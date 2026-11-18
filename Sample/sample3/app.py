"""Stock-related news search with an explicit offline demonstration mode."""
import os
from flask import Flask, render_template, request
from naver import NaverError, search_news

app = Flask(__name__)
app.config['NAVER_CLIENT_ID'] = os.getenv('NAVER_CLIENT_ID', '')
app.config['NAVER_CLIENT_SECRET'] = os.getenv('NAVER_CLIENT_SECRET', '')

@app.get('/')
def index():
    query = request.args.get('q', '삼성전자 주식').strip()
    mode = request.args.get('mode', 'demo')
    items, error, status = [], None, 200
    if not query or len(query) > 100 or mode not in ('demo', 'live'):
        error, status = '검색어는 1~100자, 모드는 demo 또는 live여야 합니다.', 400
    elif mode == 'demo':
        items = [{'title': f'[가상 뉴스] {query} 관련 수업 예시',
                  'description': '실제 기사나 API 응답이 아닙니다. 실제 API 모드를 선택하여 뉴스를 검색하세요.',
                  'date': '가상 수업 데이터', 'link': ''}]
    elif not app.config['NAVER_CLIENT_ID'] or not app.config['NAVER_CLIENT_SECRET']:
        error, status = 'NAVER_CLIENT_ID와 NAVER_CLIENT_SECRET 환경변수를 설정하세요.', 503
    else:
        try:
            items = search_news(query, app.config['NAVER_CLIENT_ID'], app.config['NAVER_CLIENT_SECRET'])
        except NaverError as exc:
            error, status = str(exc), 502
    return render_template('index.html', query=query, mode=mode, items=items,
                           error=error), status

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003)
