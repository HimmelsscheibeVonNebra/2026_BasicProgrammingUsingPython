"""Flask routes: input → analysis → escaped Jinja view."""
from pathlib import Path
from flask import Flask, render_template, request
from logic import MARKETS, analyze, summarize
from storage import load_quotes

BASE = Path(__file__).resolve().parent
app = Flask(__name__)
app.config['DATA_PATH'] = BASE / 'data/prices.csv'

@app.get('/')
def index():
    market = request.args.get('market', 'ALL')
    rows, summary, day, error, status = [], summarize([]), None, None, 200
    try:
        quotes = load_quotes(app.config['DATA_PATH'])
        rows = analyze(quotes, market)
        summary = summarize(rows)
        day = quotes[0]['date'] if quotes else None
    except ValueError as exc:
        error, status = str(exc), 400
    except OSError:
        error, status = '데이터 파일을 읽을 수 없습니다.', 500
    return render_template('index.html', title='미국 주식 분석',
        currency='USD', scale=100, database=False,
        markets=MARKETS, market=market, rows=rows, summary=summary,
        day=day, error=error), status

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
