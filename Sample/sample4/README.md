# Sample 4: SQLite 주가 저장·분석

Python 3.10 이상과 Flask를 사용합니다. 이 폴더만 복사해도 실행할 수 있습니다.

## 실행

저장소 루트에서:

```bash
cd Sample/sample4
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
flask --app app init-db
python app.py
```

Windows PowerShell에서는 활성화 명령을 `.venv\Scripts\Activate.ps1`로 바꿉니다.
브라우저에서 http://127.0.0.1:5004 을 엽니다. Ctrl+C로 종료합니다.

## 실습 흐름

1. `data/prices.csv`를 확인합니다. 모든 수치는 2026-11-05 기준 **가상 수업 데이터**입니다.
2. 웹에서 시장을 선택하여 등락률 순위와 상승·하락·보합 수를 비교합니다.
3. CSV의 종가를 바꾸어 다시 조회합니다. SQLite 예제는 변경 후 `flask --app app init-db`로 다시 가져와야 반영됩니다.
4. 0인 가격이나 중복 코드를 넣고 오류 처리를 확인합니다.

등락률 = (종가 − 전일 종가) / 전일 종가 × 100. 같은 가격 기준을 사용하며,
계산값은 유지하고 화면에서만 소수 둘째 자리로 표시합니다.
평균은 선택된 종목의 동일 가중 표본 평균이며 시장 지수 수익률이 아닙니다.

`app.py`: HTTP 요청과 오류 처리 → `storage.py`: CSV 읽기 → `logic.py`: 검증·분석 → `templates/index.html`: Jinja 렌더링.
Jinja 자동 escaping을 사용하며 종목명에 HTML을 넣어도 실행하지 않습니다.
헤더만 있는 CSV는 유효한 빈 표본(평균 N/A), 파일 누락은 오류입니다.

한국 가격은 정수 원(KRW), 거래량은 정수 주입니다. 005930 같은 코드를 문자열로 유지합니다. ALL 평균 +0.40%, KOSPI +0.33%, KOSDAQ +0.50%입니다.

## SQLite

`database.py`가 Python 표준 라이브러리 sqlite3를 사용합니다. 별도 DB 서버가 필요 없습니다.
`flask --app app init-db`가 CSV 전체를 검증한 후 `instance/market.sqlite3`를 만듭니다.
웹 요청은 CSV 대신 SQLite를 조회합니다. 초기화 전에는 안내 오류를 보여 줍니다.
재실행하면 기존 스냅샷을 한 트랜잭션에서 교체하며, 검증/쓰기 실패 시 기존 데이터가 보존됩니다.
SQL에는 매개변수 바인딩을 사용합니다. 종목 코드는 TEXT 기본키입니다.
이 예제는 단일 날짜 스냅샷 저장이며 여러 날짜의 가격 이력은 저장하지 않습니다.

```bash
python -m sqlite3 instance/market.sqlite3 "SELECT code, name, close FROM quotes;"
```

위 조회 CLI는 Python 3.12 이상에서 사용할 수 있습니다.
