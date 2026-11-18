# Sample 3: 네이버 주식 뉴스 API

Python 3.10 이상과 Flask를 사용합니다. 이 폴더만 복사해도 실행할 수 있습니다.

## 실행

저장소 루트에서:

```bash
cd Sample/sample3
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Windows PowerShell에서는 활성화 명령을 `.venv\Scripts\Activate.ps1`로 바꿉니다.
브라우저에서 http://127.0.0.1:5003 을 엽니다. Ctrl+C로 종료합니다.

## 네이버 연결

기본 모드는 키 없이 동작하는 **명시적인 가상 뉴스 데모**입니다.
실제 기사를 검색하려면 네이버 개발자 센터에서 애플리케이션에 검색 API 사용 권한을 설정하고 키를 발급합니다.
서버 실행 전에 환경변수를 설정합니다 (`.env.example`은 이름 안내이며 자동 로드하지 않습니다).

```bash
export NAVER_CLIENT_ID='발급받은-client-id'
export NAVER_CLIENT_SECRET='발급받은-client-secret'
python app.py
```

PowerShell: `$env:NAVER_CLIENT_ID='...'`, `$env:NAVER_CLIENT_SECRET='...'`.
화면의 데이터 선택을 **실제 API**로 바꾸고 종목명을 검색합니다.
키는 서버에서만 사용하며 저장소에 올리지 않습니다.

`app.py` → `naver.py` → 네이버 뉴스 검색 JSON API → Jinja 화면.
최신순으로 최대 10건을 보여 줍니다. 뉴스 결과 자체를 조회하며 주가·감성 점수나 매매 신호를 계산하지 않습니다.
키 누락(503), 잘못된 검색어(400), 인증·통신·응답 오류(502)를 화면에 표시합니다.
10초 timeout을 적용하며 API 실패를 가상 뉴스로 대체하지 않습니다.
기사 HTML 강조 태그를 제거하고 텍스트는 Jinja로 escaping합니다.

공식 문서: https://developers.naver.com/docs/serviceapi/search/news/news.md
