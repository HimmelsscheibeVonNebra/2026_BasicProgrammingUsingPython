# 실습: 한국 증권시장 분석 → 웹 보고서

18분. 참고 완성본은 `examples/korea_market_mvp/`입니다. 자신의 프로젝트에서는 같은 문서·구현 연결 방식을 적용합니다. 완성본을 복사한 것과 직접 구현한 부분을 PR에 구분해서 적습니다.

## 제공 첨부 문서

- [team-name_user-scenario.md](team-name_user-scenario.md): SC-01 정상 / SC-02 오류 / SC-03 빈 데이터와 아키텍처.
- [team-name_spec.xlsx](team-name_spec.xlsx): Requirement·Feature·Function·Test를 채운 예시. Function의 시스템 호출 열은 Python 표준 라이브러리·I/O로 바꿨다.

실제 제출 시 예시 작성자 정보와 테스트 결과를 본인의 것으로 갱신한다. 1인 프로젝트이며 별도 프로세스·IPC를 구현할 필요는 없다. TEST-13 브라우저 검증은 직접 확인 전까지 Not run이다.

## 1. 설계 추적 (4분)

`project-spec.md`를 열고 REQ-03 또는 REQ-06을 선택합니다.

```text
관련 SC (시나리오):
내가 선택한 REQ:
연결된 FEAT:
호출되는 FUNC ID, 함수와 모듈:
UML에서 해당 호출 또는 오류 분기:
검증할 TEST와 입력/기대 결과:
```

REQ-03을 고르면 `feature/feat02-market-analysis` 브랜치를 만들고 등락률·필터·정렬·요약 중 아직 fake인 부분을 구현합니다. REQ-06을 고르면 `feature/feat03-safe-report`에서 오류 처리와 출력 보존을 구현합니다. 먼저 작은 HTML이나 출력까지 연결해 실행 가능한 상태를 유지합니다.

## 2. 한 슬라이스 구현 (9분)

- 함수 계약을 읽고 fake 하나를 실제 본문으로 교체합니다.
- 순수 분석 함수에는 print/input/open을 넣지 않습니다.
- `python3 -m unittest -v`로 관련 테스트를 확인하고 `python3 main.py`로 전체를 실행합니다.
- `--market KOSPI`의 종목 3개와 평균 +0.33%를 확인합니다.
- `docs/index.html`을 브라우저로 열어 한글·단위·부호·기준일·가상 데이터 표시를 봅니다.
- 음수 가격이나 0 전일종가를 가진 별도 CSV를 만들어 오류와 기존 HTML 보존을 확인합니다. 원본 예제 CSV는 그대로 둡니다.

```bash
cd 11week/examples/korea_market_mvp
python3 -m unittest -v
python3 main.py
python3 main.py --market KOSPI
python3 main.py --market ALL
python3 -m http.server 8000 --directory docs --bind 127.0.0.1
```

http://localhost:8000 에 접속합니다. 시장 변경은 CLI 재생성 후 브라우저 새로고침입니다. 서버를 종료하려면 Ctrl+C를 누릅니다. 헤더만 있는 CSV는 빈 보고서를 만들지만, 누락 파일은 오류입니다.

## 3. 검토와 PR (5분)

한 가지 리팩터링만 적용하고 테스트를 다시 실행합니다. 브랜치를 push하고 PR을 엽니다. 저장소가 없는 배포 ZIP에서 실습한다면 자신의 프로젝트 저장소로 필요한 파일을 복사한 뒤 Git 작업을 합니다.

```text
## What
FEAT-02 / REQ-03: KOSPI 필터와 등락률 정렬 구현
## Why
시장별 비교를 웹 보고서에 표시하기 위한 Must 기능
## How I checked
python3 -m unittest -v: 관련 테스트 통과
python3 main.py --market KOSPI: 3종목, 평균 +0.33%
브라우저 화면 캡처 첨부
## Remaining
미구현 fake와 다음 PR 범위 (없으면 없음)
```

제출: 작성한 `team-name_spec.xlsx`, `team-name_user-scenario.md`, UML, 구현 코드, 테스트 결과, 생성 HTML, 브라우저 캡처, PR 링크. 완성 MVP에는 Must 경로의 fake/TODO가 없어야 합니다. API·차트·클릭 필터는 후속 과제입니다.
