"""NAVER News Search API client; credentials stay on the server."""
import html
import json
import re
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlsplit
from urllib.request import Request, urlopen


class NaverError(Exception):
    pass


def plain_text(value):
    return html.unescape(re.sub(r'<[^>]*>', '', value))


def search_news(query, client_id, client_secret):
    params = urlencode({'query': query, 'display': 10, 'start': 1, 'sort': 'date'})
    request = Request('https://openapi.naver.com/v1/search/news.json?' + params,
                      headers={'X-Naver-Client-Id': client_id,
                               'X-Naver-Client-Secret': client_secret})
    try:
        with urlopen(request, timeout=10) as response:
            payload = json.load(response)
        items = []
        for row in payload['items']:
            link = row.get('originallink') or row.get('link', '')
            if urlsplit(link).scheme not in ('http', 'https'):
                link = ''
            items.append({'title': plain_text(row['title']),
                          'description': plain_text(row['description']),
                          'date': row['pubDate'], 'link': link})
        return items
    except HTTPError as exc:
        raise NaverError(f'네이버 API 오류 HTTP {exc.code}. 키와 검색 API 권한을 확인하세요.') from exc
    except (URLError, TimeoutError, OSError, ValueError, KeyError, TypeError) as exc:
        raise NaverError('네이버 뉴스 응답을 가져오지 못했습니다. 잠시 후 다시 시도하세요.') from exc
