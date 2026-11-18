"""Flask routes: input → analysis → escaped Jinja view."""
from pathlib import Path
from flask import Flask, render_template, request
from logic import MARKETS, analyze, summarize
from storage import load_quotes
from database import read_quotes, import_snapshot
import sqlite3

BASE = Path(__file__).resolve().parent
app = Flask(__name__)
app.config['DATA_PATH'] = BASE / 'data/prices.csv'
app.config['DATABASE'] = BASE / 'instance/market.sqlite3'

@app.get('/')
def index():
    market = request.args.get('market', 'ALL')
    rows, summary, day, error, status = [], summarize([]), None, None, 200
    try:
        quotes = read_quotes(app.config['DATABASE'])
        rows = analyze(quotes, market)
        summary = summarize(rows)
        day = quotes[0]['date'] if quotes else None
    except ValueError as exc:
        error, status = str(exc), 400
    except (OSError, sqlite3.Error):
        error, status = 'DB를 읽을 수 없습니다. 먼저 flask --app app init-db를 실행하세요.', 500
    return render_template('index.html', title='SQLite 한국 주식 분석',
        currency='KRW', scale=1, database=True,
        markets=MARKETS, market=market, rows=rows, summary=summary,
        day=day, error=error), status

@app.cli.command('init-db')
def init_db():
    """Validate CSV, then transactionally replace the stored snapshot."""
    quotes = load_quotes(app.config['DATA_PATH'])
    analyze(quotes, 'ALL')
    import_snapshot(app.config['DATABASE'], quotes)
    print(f"Imported {len(quotes)} quotes.")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5004)
