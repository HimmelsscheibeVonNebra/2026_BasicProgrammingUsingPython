# User Scenarios — 한국 증권시장 분석 웹 보고서

| Item | Details |
|---|---|
| Team name | Korea Market / 1인 수업 예시 |
| Team members (name / student ID) | 실제 제출 시 본인 이름 / 학번 기입 |
| 예제 작성일 | 2026-11-06 |
| Document version | v2 / 수업용 작성 예시 |

첨부된 사용자 시나리오 양식의 항목을 시장 분석 프로젝트로 채운 예제다. 관련 명세는 같은 폴더의 [team-name_spec.xlsx](team-name_spec.xlsx)이며 Requirement 시트의 Related scenarios 열에서 SC-01~03을 참조한다. 명령은 저장소 루트에서 `cd 11week/examples/korea_market_mvp` 후 실행한다.

## 1. Project Overview

학생은 한국 주식 표본의 전일·당일 종가와 거래량을 CSV로 준비한다. Python 프로그램은 입력을 검증하고 일간 등락률, 시장별 순위, 상승·하락·보합 수와 표본 단순평균을 계산한다. 계산 결과는 한글 HTML로 생성하여 브라우저에서 확인한다. 제공 가격·거래량은 **수업용 가상 데이터**이며 실제 시세나 현재 상장 종목 목록이 아니다. 실시간 API·기간 분석·차트·브라우저 클릭 필터는 이번 MVP에서 구현하지 않는다.

## 2. Users

| User | Description |
|---|---|
| 학생 민지 | CSV를 준비하고 시장을 선택하여 분석 보고서를 생성·확인한다. |
| 동료 검토자 / 교수자 | 동일한 CSV·명령·테스트로 요구사항과 결과를 재현한다. |

## 3. Scenarios

### SC-01. 시장별 분석 결과를 웹페이지로 확인한다

- **User**: 학생 민지
- **Context**: 한 날짜의 KOSPI·KOSDAQ 표본 CSV를 준비했다. 두 종가는 같은 가격 기준이다.
- **Goal**: 전체 표본과 KOSPI 표본을 등락률 순서로 비교한다.
- **Related requirements**: REQ-01~05. REQ-07/08은 이 상황에서 출발하는 후속 아이디어이며 현재 수락 조건에 포함하지 않는다.

**Workflow**

1. 민지는 `data/prices.csv`를 확인한다. 종목코드는 선행 0이 있는 문자열이며 가격·거래량은 정수다.
2. ALL 보고서를 생성한다. 프로그램은 파일·헤더·행·단일 날짜·중복 코드를 검증한다.
3. 프로그램이 등락률을 계산하고 내림차순으로 정렬한다. 동률은 코드 오름차순이다.
4. 민지는 `docs/index.html`을 브라우저로 열어 기준일, 시장, 가상 데이터 출처, 요약과 표를 확인한다.
5. `--market KOSPI`로 다시 생성하고 브라우저를 새로고침한다. 시장 선택은 CLI에서 이루어진다.

**Example Execution**

```bash
$ python3 main.py --market ALL --output docs/index.html
Generated docs/index.html (5 stocks)
$ python3 main.py --market KOSPI --output docs/index.html
Generated docs/index.html (3 stocks)
```

**Expected web result**

| 시장 | 순서 / 등락률 | 표본 요약 |
|---|---|---|
| ALL | 247540 +3%, 005930 +2%, 035420 0%, 000660 -1%, 035900 -2% | 5개, 상승 2·하락 2·보합 1, 평균 +0.40% |
| KOSPI | 005930 +2%, 035420 0%, 000660 -1% | 3개, 상승 1·하락 1·보합 1, 평균 +0.33% |

화면에서는 등락률을 부호 포함 소수 2자리로 표시한다. 평균은 표본의 동일 가중 평균이며 KOSPI/KOSDAQ 지수 등락률이 아니다.

**Outcome**: 선택한 시장의 보고서가 저장되고 민지가 브라우저로 확인한다. 입력 CSV는 변하지 않는다. 자동 검증: TEST-01/02/04/05/08/11/12. 브라우저 시각 검증: TEST-13, 수업에서 직접 확인.

### SC-02. 전일종가가 0인 입력을 거부하고 기존 보고서를 보존한다

- **User**: 학생 민지
- **Context**: SC-01에서 정상 보고서를 생성한 후, 잘못된 전일종가가 들어 있는 별도 파일을 전달한다.
- **Expected behavior**: CSV 행 번호와 원인을 알리고 종료 코드 1로 끝낸다. 기존 HTML과 원본 CSV는 바뀌지 않는다.
- **Related requirements**: REQ-02, REQ-06

**Workflow**

1. 정상 보고서의 내용을 확인한다.
2. 민지는 제공된 `data/invalid-zero.csv`를 입력으로 지정한다. 첫 종목의 전일종가가 0이다.
3. `load_quotes`가 두 번째 CSV 행을 `parse_row`로 검증하다 ValueError를 받는다.
4. `main`이 오류를 출력한다. 분석·렌더링·최종 HTML 교체는 수행하지 않는다.
5. 민지는 기존 보고서를 유지한 채 입력 파일을 수정한다. 출력 도중 오류가 생기는 경우에도 임시 파일을 정리하고 이전 결과를 보존한다.

**Example Execution**

```bash
$ python3 main.py --output docs/index.html
Generated docs/index.html (5 stocks)
$ python3 main.py --input data/invalid-zero.csv --output docs/index.html
Report not generated: CSV row 2: previous_close must be >= 1
```

**Outcome**: 종료 코드 1, 기존 HTML 불변. 데이터 오류 검증은 TEST-03/07, 누락·잘못된 파일과 보존은 TEST-09, 출력 교체 오류·임시 파일 정리는 TEST-10에 연결된다. 실패 후 열린 브라우저 화면은 이전 결과이므로 기준일과 CLI 오류 메시지를 함께 확인한다.

### SC-03. 정상 헤더만 있는 CSV로 빈 보고서를 만든다

- **User**: 동료 검토자
- **Context**: 데이터가 없는 정상 입력과 파일 누락을 구분해 검증하려 한다.
- **Goal**: 프로그램이 정상적인 빈 상태를 명확히 보여주는지 확인한다.
- **Related requirements**: REQ-01, REQ-04, REQ-05

**Workflow**

1. 검토자는 정상 헤더만 있는 `data/empty.csv`로 별도 보고서를 생성한다.
2. 프로그램은 빈 목록을 정상 입력으로 취급한다.
3. 웹페이지에 종목 0개, 상승·하락·보합 0, 평균 N/A, 빈 종목 안내, 기준일 '데이터 없음'을 표시한다.
4. 파일 자체가 없으면 SC-02와 같은 오류 경로로 종료함을 구분한다.

**Example Execution**

```bash
$ python3 main.py --input data/empty.csv --output docs/empty.html
Generated docs/empty.html (0 stocks)
```

**Outcome**: 빈 상태 HTML 생성, 종료 코드 0. TEST-06/12와 연결된다. 빈 화면의 시각 확인은 TEST-13에서 수행한다.

## 4. System Architecture

### 4.1 Processes and Threads

```text
[학생 CLI] -> [Python main: 단일 프로세스·메인 스레드]
                |-> storage.load_quotes -> logic.parse_row
                |-> logic.analyze -> logic.summarize
                |-> report.render_html
                `-> storage.write_html -> docs/index.html

[브라우저] -> 생성된 HTML 파일 열기
선택: [python -m http.server] -> 정적 HTML 제공 (분석을 실행하지 않음)
```

| Process / Thread | Role | Creation / Termination |
|---|---|---|
| Python CLI / 메인 스레드 | CSV 검증·분석·HTML 생성 | `python3 main.py`; 성공 0, 데이터/I/O 실패 1, CLI 인자 오류 2로 종료 |
| 브라우저 | 생성된 파일 표시 | 사용자가 파일을 연다. CLI와 별도 프로그램이며 자식 프로세스로 만들지 않음 |
| 로컬 HTTP 서버 (선택) | docs 폴더의 정적 파일 제공 | 별도 터미널에서 실행, Ctrl+C 종료. Python 분석 백엔드가 아님 |

fork·자식 프로세스·작업 스레드·서버 프레임워크는 사용하지 않는다.

### 4.2 IPC and Synchronization

| Where Used | Method | Reason |
|---|---|---|
| 모듈 간 | 일반 함수 인자와 반환값 | 단일 Python 프로세스이므로 IPC 없음 |
| HTML 출력 | 같은 디렉터리의 임시 파일 작성 후 `os.replace` | 작성 실패가 기존 보고서를 훼손하지 않도록 함 |
| 동시 생성 | 지원 범위 밖, 같은 경로에 한 번에 한 프로세스만 실행 | 파일 잠금·다중 작성자 동기화는 구현하지 않음 |

### 4.3 Data Storage Format

| File / Data | Format (Text / Binary) | Structure |
|---|---|---|
| `data/prices.csv` | UTF-8 text (BOM 허용) | `date,code,name,market,previous_close,close,volume`; 단일 날짜·중복 없는 코드 |
| `data/invalid-zero.csv` | UTF-8 text | 같은 구조, 첫 종목 전일종가 0인 오류 실습 파일 |
| `data/empty.csv` | UTF-8 text | 정상 헤더만 존재 |
| `docs/index.html` | UTF-8 HTML | 한글 제목·기준일·시장·출처·표본 요약·종목 표; 외부 텍스트 escape |
| 메모리 Quote | Python dict | 날짜/코드/이름/시장 str, 가격·거래량 int; 분석 후 change_pct float 추가 |
| 메모리 Summary | Python dict | count/up/down/flat int, mean float 또는 None |

## 5. Division of Responsibilities

| Team Member | Responsibility |
|---|---|
| 1인 작성자 (실제 제출 시 본인 이름으로 변경) | SC-01~03, REQ-01~08, FEAT-01~03, FUNC-01~08, TEST-01~13, UML·README·구현·PR |
| 동료 검토자 | 추적성·실행 재현 검토; 구현 책임을 대신하지 않음 |

## 6. Additional Notes

- 상세 함수 계약·UML 원본은 [project-spec.md](../../examples/korea_market_mvp/project-spec.md)를 참조한다.
- `python3 -m unittest -v`로 자동 테스트 12개를 실행한다. 엑셀 Test 시트는 실행 명령·기대값·실제 결과·상태를 구분한다.
- TEST-13은 실제 브라우저 확인 전까지 Not run이다. 자동 테스트 PASS가 시각 검증 완료를 의미하지 않는다.
- 선택적 로컬 열람: `python3 -m http.server 8000 --directory docs --bind 127.0.0.1`, 접속 http://localhost:8000, 종료 Ctrl+C.
- 입력 오류 후 기존 파일을 보는 경우 새 분석이 성공한 것으로 간주하지 않는다. 실제 제출 시 이름·학번·제출일과 재실행 결과를 갱신한다.
