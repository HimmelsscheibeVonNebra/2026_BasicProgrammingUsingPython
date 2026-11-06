"""REQ-linked checks: python3 -m unittest -v."""
import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from logic import analyze, change_pct, parse_row, summarize
from main import BASE, main
from report import render_html
from storage import load_quotes, write_html


class MarketTests(unittest.TestCase):
    def setUp(self):
        self.quotes = load_quotes(BASE / 'data/prices.csv')

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

    def test_09_missing_and_bad_csv_preserve_report(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            output = root / 'index.html'
            output.write_text('OLD', encoding='utf-8')
            bad = root / 'bad.csv'
            bad.write_text('wrong,header\n1,2\n', encoding='utf-8')
            for source in [root / 'missing.csv', bad]:
                with contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(main(['--input', str(source), '--output', str(output)]), 1)
                self.assertEqual(output.read_text(), 'OLD')

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
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(main(['--market', 'KOSPI', '--output', str(output)]), 0)
            html = output.read_text(encoding='utf-8')
            self.assertIn('삼성전자', html)
            self.assertNotIn('에코프로비엠', html)
            self.assertIn('종목 3개', html)

    def test_12_csv_boundaries(self):
        header = 'date,code,name,market,previous_close,close,volume\n'
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / 'prices.csv'
            source.write_text('\ufeff' + header, encoding='utf-8')
            self.assertEqual(load_quotes(source), [])
            for tail in ['2026-11-05,005930,삼성전자,KOSPI,70000,71400\n',
                         '2026-11-05,005930,삼성전자,KOSPI,70000,71400,0,extra\n']:
                source.write_text(header + tail, encoding='utf-8')
                with self.assertRaises(ValueError):
                    load_quotes(source)


if __name__ == '__main__':
    unittest.main()
