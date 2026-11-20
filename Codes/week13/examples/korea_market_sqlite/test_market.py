"""REQ-linked checks: python3 -m unittest -v."""
import contextlib
import io
import sqlite3
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from logic import analyze, change_pct, parse_row, summarize
from main import BASE, main
from report import render_html
from storage import (connect, init_db, load_quotes, read_csv,
                     replace_quotes, write_html)


class MarketTests(unittest.TestCase):
    def setUp(self):
        self.quotes = read_csv(BASE / 'data/prices.csv')

    def test_01_schema_and_leading_zero(self):
        self.assertEqual(self.quotes[0]['code'], '005930')
        self.assertEqual(self.quotes[0]['close'], 71400)

    def test_02_changes(self):
        for previous, close, expected in [(70000, 71400, 2), (200000, 198000, -1), (100, 100, 0)]:
            self.assertAlmostEqual(change_pct(previous, close), expected)

    def test_03_reject_invalid_fields(self):
        row = {k: str(v) for k, v in self.quotes[0].items()}
        for field, bad in [('previous_close', '0'), ('close', '-1'), ('volume', '-1'),
                           ('close', 'NaN'), ('volume', '1.5'), ('code', '5930'),
                           ('date', '2026-02-30'), ('name', ''), ('market', 'OTHER')]:
            with self.subTest(field=field, bad=bad), self.assertRaises(ValueError):
                parse_row(dict(row, **{field: bad}))

    def test_04_filter_and_sort(self):
        rows = analyze(self.quotes, 'KOSPI')
        self.assertEqual([q['code'] for q in rows], ['005930', '035420', '000660'])
        self.assertNotIn('change_pct', self.quotes[0])
        tied = [dict(self.quotes[0], code='000002'), dict(self.quotes[0], code='000001')]
        self.assertEqual(analyze(tied, 'ALL')[0]['code'], '000001')
        with self.assertRaises(ValueError):
            analyze(self.quotes, 'OTHER')

    def test_05_sample_summary(self):
        summary = summarize(analyze(self.quotes, 'ALL'))
        self.assertEqual((summary['count'], summary['up'], summary['down'], summary['flat']), (5, 2, 2, 1))
        self.assertAlmostEqual(summary['mean'], 0.4)

    def test_06_empty_data(self):
        for rows in [analyze([], 'ALL'), analyze(self.quotes[:1], 'KOSDAQ')]:
            summary = summarize(rows)
            self.assertIsNone(summary['mean'])
            html = render_html(rows, summary, 'KOSDAQ', '데이터 없음')
            self.assertIn('표시할 종목이 없습니다', html)
            self.assertIn('N/A', html)

    def test_07_snapshot_identity(self):
        for rows in [self.quotes + [self.quotes[0]],
                     [self.quotes[0], dict(self.quotes[1], date='2026-11-04')]]:
            with self.assertRaises(ValueError):
                analyze(rows, 'ALL')

    def test_08_html_escape(self):
        rows = analyze([dict(self.quotes[0], name='<script>alert(1)</script>')], 'ALL')
        html = render_html(rows, summarize(rows), 'ALL', '2026-11-05')
        self.assertNotIn('<script>', html)
        self.assertIn('&lt;script&gt;', html)
        self.assertIn('+2.00%', html)
        self.assertIn('71,400', html)
        self.assertIn('005930', html)

    def test_09_failed_import_preserves_report_and_rows(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            db = root / 'market.db'
            output = root / 'index.html'
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(main(['--db', str(db), '--output', str(output),
                                       '--import-csv', str(BASE / 'data/prices.csv')]), 0)
            output.write_text('OLD', encoding='utf-8')
            bad = root / 'bad.csv'
            bad.write_text('wrong,header\n1,2\n', encoding='utf-8')
            for source in [root / 'missing.csv', bad, BASE / 'data/invalid-zero.csv']:
                with contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(main(['--db', str(db), '--output', str(output),
                                           '--import-csv', str(source)]), 1)
                self.assertEqual(output.read_text(), 'OLD')
                with contextlib.closing(connect(db)) as con:
                    self.assertEqual(len(load_quotes(con)), 5)

    def test_10_atomic_write_failure(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / 'index.html'
            output.write_text('OLD')
            with patch('storage.os.replace', side_effect=OSError('simulated failure')):
                with self.assertRaises(OSError):
                    write_html(output, 'NEW')
            self.assertEqual(output.read_text(), 'OLD')
            self.assertEqual(list(Path(folder).iterdir()), [output])

    def test_11_end_to_end(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / 'docs/index.html'
            db = Path(folder) / 'data/market.db'
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(main(['--db', str(db), '--import-csv', str(BASE / 'data/prices.csv'),
                                       '--market', 'KOSPI', '--output', str(output)]), 0)
                # A second run reads the stored rows; no CSV is needed.
                self.assertEqual(main(['--db', str(db), '--market', 'KOSPI', '--output', str(output)]), 0)
            html = output.read_text(encoding='utf-8')
            self.assertIn('삼성전자', html)
            self.assertNotIn('에코프로비엠', html)
            self.assertIn('종목 3개', html)

    def test_12_csv_boundaries(self):
        header = 'date,code,name,market,previous_close,close,volume\n'
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / 'prices.csv'
            source.write_text('\ufeff' + header, encoding='utf-8')
            self.assertEqual(read_csv(source), [])
            for tail in ['2026-11-05,005930,삼성전자,KOSPI,70000,71400\n',
                         '2026-11-05,005930,삼성전자,KOSPI,70000,71400,0,extra\n']:
                source.write_text(header + tail, encoding='utf-8')
                with self.assertRaises(ValueError):
                    read_csv(source)


class StorageTests(unittest.TestCase):
    """Week 13: the storage layer, checked against an in-memory database."""

    def setUp(self):
        self.con = connect(':memory:')
        init_db(self.con)
        self.quotes = read_csv(BASE / 'data/prices.csv')

    def tearDown(self):
        self.con.close()

    def test_13_empty_table_is_empty_list(self):
        self.assertEqual(load_quotes(self.con), [])

    def test_14_round_trip_keeps_types(self):
        replace_quotes(self.con, self.quotes)
        stored = load_quotes(self.con)
        self.assertEqual(stored, sorted(self.quotes, key=lambda q: q['code']))
        self.assertEqual(stored[0]['code'], '000660')
        self.assertIsInstance(stored[0]['close'], int)

    def test_15_replace_does_not_append(self):
        replace_quotes(self.con, self.quotes)
        replace_quotes(self.con, self.quotes[:2])
        self.assertEqual(len(load_quotes(self.con)), 2)

    def test_16_failed_replace_keeps_old_rows(self):
        replace_quotes(self.con, self.quotes)
        for bad in [self.quotes[:1] * 2,                      # duplicate key
                    [dict(self.quotes[0], close=0)],          # CHECK
                    [dict(self.quotes[0], name=None)]]:       # NOT NULL
            with self.subTest(bad=bad), self.assertRaises(sqlite3.IntegrityError):
                replace_quotes(self.con, bad)
            self.assertEqual(len(load_quotes(self.con)), 5)

    def test_17_same_analysis_from_csv_and_database(self):
        replace_quotes(self.con, self.quotes)
        self.assertEqual(analyze(load_quotes(self.con), 'ALL'), analyze(self.quotes, 'ALL'))

    def test_18_init_db_twice_keeps_rows(self):
        replace_quotes(self.con, self.quotes)
        init_db(self.con)
        self.assertEqual(len(load_quotes(self.con)), 5)


if __name__ == '__main__':
    unittest.main()
