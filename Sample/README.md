# Week 11 Session 2 — Flask 프로젝트 예제

강의 `11week/week11-session2.md`의 검증 → 분석 → HTML 흐름을 Flask 웹 앱으로 확장한 독립 프로젝트입니다.

| 폴더 | 학습 주제 | 데이터 | 주소 |
|---|---|---|---|
| sample1 | 미국 주식: NASDAQ/NYSE 필터·등락률·요약 | 가상 CSV, 정수 센트 → USD | http://127.0.0.1:5001 |
| sample2 | 한국 주식: KOSPI/KOSDAQ 필터·등락률·요약 | 가상 CSV, KRW | http://127.0.0.1:5002 |
| sample3 | 네이버 API 인증·뉴스 검색·실패 처리 | 가상 데모 또는 실제 뉴스 API | http://127.0.0.1:5003 |
| sample4 | SQLite 저장·조회·트랜잭션 | 가상 CSV → SQLite, KRW | http://127.0.0.1:5004 |

각 폴더의 README에 설치·실행·실습 방법이 있습니다. Python 3.10 이상을 사용합니다.
각 프로젝트는 별도 가상환경에서 `pip install -r requirements.txt` 후 `python app.py`로 실행합니다.
**sample4는 실행 전에 `flask --app app init-db`가 필요합니다.**

sample1/2/4는 외부 주가 API 없이 실행되며 가격은 실시간 시세가 아닙니다.
sample3은 뉴스 API 연동 예제이며 실제 API 모드에는 개인 네이버 API 키와 네트워크가 필요합니다.

학습 순서: sample2로 강의와 비교 → sample1의 통화·코드 차이 → sample3의 외부 I/O → sample4의 영속 저장.

## 검증

Flask가 설치된 가상환경에서 저장소 루트 기준으로 실행합니다.

```bash
python Sample/verify.py
```

네 프로젝트를 별도 프로세스로 검사합니다. 시장 필터·표본 평균·잘못된 입력·빈 데이터·HTML escaping,
네이버 API 모의 성공/실패, SQLite 초기화·재저장 시 검증 실패에 대한 데이터 보존을 확인합니다.
검사는 임시 DB를 사용하며 외부 API를 호출하지 않습니다. 실제 네이버 연결은 개인 키로 별도 확인해야 합니다.
