"""Week 12 Session 2 experiments. Run from any directory; stdlib only.

All file experiments use disposable temporary directories. The Week 11 MVP
is imported without modifying its source or its generated report.
"""
import argparse
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
from unittest.mock import patch

MVP = Path(__file__).resolve().parents[3] / '11week/examples/korea_market_mvp'
sys.path.insert(0, str(MVP))
from logic import FIELDS
from main import main
from storage import write_html


def validate_min_volume(value):
    if type(value) is not int or value < 0:
        raise ValueError('min_volume must be a nonnegative integer')
    return value


def verdict():
    for value in (0, 100, -1, True, '100', 1.5):
        try:
            result = validate_min_volume(value)
        except ValueError as error:
            print(f'{value!r} ({type(value).__name__}): REJECT: {error}')
        else:
            print(f'{value!r} ({type(value).__name__}): ACCEPT: {result}')


def csv_experiment():
    header = ','.join(FIELDS) + '\n'
    valid = '2026-11-13,005930,Sample,KOSPI,100,110,100\n'
    # Add one case here. None represents a missing file, not an empty file.
    cases = {
        'valid': header + valid,
        'header_only': header,
        'missing': None,
        'negative_volume': header + valid.replace(',100\n', ',-1\n'),
    }
    with TemporaryDirectory() as folder:
        base = Path(folder)
        for name, content in cases.items():
            source = base / f'{name}.csv'
            output = base / 'index.html'
            if content is not None:
                source.write_text(content, encoding='utf-8')
            output.write_text('OLD', encoding='utf-8')
            print(f'\nCASE: {name}')
            code = main(['--input', str(source), '--output', str(output)])
            preserved = output.read_text(encoding='utf-8') == 'OLD'
            print(f'return={code}; OLD preserved={preserved}')


def rescue():
    with TemporaryDirectory() as folder:
        output = Path(folder) / 'index.html'
        output.write_text('OLD', encoding='utf-8')
        with patch('storage.os.replace', side_effect=OSError('simulated failure')):
            try:
                write_html(output, 'NEW')
            except OSError as error:
                print(f'exception propagated: {error}')
        print(f'output={output.read_text(encoding="utf-8")!r}')
        print(f'files left={sorted(p.name for p in Path(folder).iterdir())}')
    # Student task: express these three observations as unittest assertions.


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('activity', choices=['verdict', 'csv', 'rescue'])
    args = parser.parse_args()
    {'verdict': verdict, 'csv': csv_experiment, 'rescue': rescue}[args.activity]()
