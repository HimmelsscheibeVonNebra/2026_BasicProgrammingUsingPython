# 13주차 2차 실습 — 저장 계층 교체

이름 / 학번:

작업 폴더: `13week/examples/korea_market_sqlite` (복사본 또는 개인 저장소의 브랜치) · 제출: 이 파일, 변경한 코드, PR 링크 또는 로컬 diff

## A. 통과에서 시작 (4분)

```bash
python3 -m unittest
python3 main.py --import-csv data/prices.csv
python3 main.py --market KOSPI
```

- 테스트 결과(개수와 OK 여부):
- `storage.py`에서 SQLite를 쓰는 함수 이름:

## B. 시장 필터를 SQL로 (12분)

`load_quotes(con, market="ALL")`이 되도록 고친다.

- `market`이 `"ALL"`이면 모든 행, 아니면 `WHERE market = ?`로 고른 행을 돌려준다.
- `load_quotes(con)`처럼 `market` 없이 부르는 기존 코드가 그대로 동작해야 한다.

내가 쓴 쿼리:

## C. `:memory:` 테스트 (8분)

`StorageTests`에 테스트를 추가한다.

| 입력 | 기대 결과 | 통과 |
|---|---|---|
| `load_quotes(con, "KOSPI")` | 3행, 모두 KOSPI | |
| `load_quotes(con, "ALL")` | 5행 | |
| `load_quotes(con)` | 5행 | |

이 테스트가 잡아내는 결함 하나(예: WHERE를 빠뜨림):

## D. 내 프로젝트의 테이블 (10분)

| 질문 | 답 |
|---|---|
| 한 행은 무엇인가? | |
| 열과 자료형(TEXT / INTEGER / REAL) | |
| 기본 키 | |
| 테이블이 거절해야 하는 값(NOT NULL, CHECK) | |

- `schema.sql`에 `CREATE TABLE IF NOT EXISTS` 문장을 쓴다.
- 저장 함수 하나와 조회 함수 하나를 만든다. 값은 `?`로 넘긴다.
- 데이터베이스가 필요 없다고 판단했다면 그 이유를 적는다.

## 제출 전 확인

- [ ] 기존 테스트 18개와 내 테스트가 모두 통과한다.
- [ ] `logic.py`와 `report.py`를 고치지 않았다.
- [ ] `.gitignore`에 `*.db`가 있고 PR에 `.db` 파일이 없다.
- [ ] 잘못된 CSV를 가져오면 테이블과 기존 HTML이 그대로다.
