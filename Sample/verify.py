"""Run with Flask installed: python Sample/verify.py. No external API or real DB used."""
from pathlib import Path
import subprocess
import sys

CHECKS = r'''
import tempfile
from pathlib import Path
from unittest.mock import patch
from app import app

app.config['TESTING'] = True
client = app.test_client()
number = NUMBER
with tempfile.TemporaryDirectory() as directory:
    temporary = Path(directory)
    if number == 3:
        from naver import NaverError, search_news
        assert client.get('/').status_code == 200
        assert client.get('/?q=').status_code == 400
        app.config.update(NAVER_CLIENT_ID='', NAVER_CLIENT_SECRET='')
        assert client.get('/?mode=live').status_code == 503
        app.config.update(NAVER_CLIENT_ID='test', NAVER_CLIENT_SECRET='test')
        with patch('app.search_news', return_value=[{'title': '<script>alert(1)</script>', 'description': 'ok', 'date': '', 'link': ''}]):
            response = client.get('/?mode=live')
            assert response.status_code == 200
            assert b'&lt;script&gt;' in response.data and b'<script>' not in response.data
        with patch('app.search_news', side_effect=NaverError('network failure')):
            assert client.get('/?mode=live').status_code == 502
        from io import BytesIO
        import json
        from urllib.error import URLError
        payload = {'items': [{'title': '<b>NAVER</b>', 'description': 'A &amp; B', 'pubDate': 'today', 'originallink': 'javascript:alert(1)'}]}
        with patch('naver.urlopen', return_value=BytesIO(json.dumps(payload).encode())) as call:
            items = search_news('삼성전자', 'id', 'secret')
            assert items[0]['title'] == 'NAVER'
            assert items[0]['description'] == 'A & B'
            assert items[0]['link'] == ''
            assert 'sort=date' in call.call_args.args[0].full_url
        with patch('naver.urlopen', side_effect=URLError('offline')):
            try:
                search_news('test', 'id', 'secret')
                raise AssertionError('network error accepted')
            except NaverError:
                pass
    else:
        from logic import analyze, summarize
        from storage import load_quotes
        source = Path('data/prices.csv')
        quotes = load_quotes(source)
        assert abs(summarize(analyze(quotes, 'ALL'))['mean'] - .4) < 1e-9
        if number == 4:
            from database import read_quotes, import_snapshot
            app.config['DATABASE'] = temporary / 'market.sqlite3'
            assert client.get('/').status_code == 500
            result = app.test_cli_runner().invoke(args=['init-db'])
            assert result.exit_code == 0, result.output
            assert read_quotes(app.config['DATABASE'])[0]['code'] == '000660'
            try:
                import_snapshot(app.config['DATABASE'], [quotes[0], quotes[0]])
                raise AssertionError('duplicate accepted')
            except ValueError:
                pass
            assert len(read_quotes(app.config['DATABASE'])) == 5
        assert client.get('/').status_code == 200
        assert b'+0.40%' in client.get('/').data
        market = 'NASDAQ' if number == 1 else 'KOSPI'
        assert client.get('/?market=' + market).status_code == 200
        if number != 1:
            assert b'+0.33%' in client.get('/?market=KOSPI').data
            assert b'005930' in client.get('/').data
        assert client.get('/?market=BAD').status_code == 400
        if number != 4:
            test_csv = temporary / 'test.csv'
            app.config['DATA_PATH'] = test_csv
            assert client.get('/').status_code == 500
            header, *rows = source.read_text().splitlines()
            test_csv.write_text(header + '\n')
            assert b'N/A' in client.get('/').data
            test_csv.write_text(source.read_text().replace(quotes[0]['name'], '<script>alert(1)</script>'))
            assert b'&lt;script&gt;' in client.get('/').data
            test_csv.write_text(header + '\n' + rows[0] + '\n' + rows[0] + '\n')
            assert client.get('/').status_code == 400
        else:
            import_snapshot(app.config['DATABASE'], [])
            assert b'N/A' in client.get('/').data
print('sample' + str(number) + ': PASS')
'''

if __name__ == '__main__':
    for number in range(1, 5):
        subprocess.run([sys.executable, '-c', CHECKS.replace('NUMBER', str(number))],
                       cwd=Path(__file__).resolve().parent / f'sample{number}', check=True)
