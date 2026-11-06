# 한국 증권시장 분석 → 웹 보고서 MVP

Python 3.9 이상과 표준 라이브러리만 사용합니다. 네트워크·API 키·패키지 설치가 필요 없습니다. 모든 가격과 거래량은 **수업용 가상 데이터**이며, 종목명·코드는 설명용 표기입니다. 현재 상장 목록이나 실제 거래일 시세를 의미하지 않습니다.

## 실행

```bash
cd 11week/examples/korea_market_mvp
python3 -m unittest -v
python3 main.py
python3 -m http.server 8000 --directory docs --bind 127.0.0.1
```

브라우저에서 http://localhost:8000 을 엽니다. 서버는 Ctrl+C로 종료합니다. `docs/index.html`을 직접 열어도 됩니다. 기본 입력·출력 경로는 main.py 위치를 기준으로 하므로 다른 작업 폴더에서도 실행할 수 있습니다.

```bash
python3 main.py --market KOSPI
python3 main.py --market KOSDAQ --output docs/kosdaq.html
python3 main.py --input data/prices.csv --market ALL
```

`--market`은 **생성 시점의 필터**입니다. 화면에서 클릭하는 동적 필터는 확장 기능입니다. ALL 보고서를 다시 만들려면 `python3 main.py`를 실행합니다. 기본 출력은 `docs/index.html`입니다. 지정한 상대 경로는 현재 작업 폴더 기준입니다. GitHub Pages에는 생성된 docs 폴더를 배포할 수 있지만 이 실습에서 자동으로 게시하지는 않습니다.

## 결과 확인

ALL: 등락률 순서 247540 (+3%), 005930 (+2%), 035420 (0%), 000660 (-1%), 035900 (-2%). 표본 5개, 상승 2·하락 2·보합 1, 단순평균 +0.40%입니다. KOSPI: 005930, 035420, 000660; 3개, 평균 +0.33%입니다. 이 평균은 표본 종목의 동일 가중 평균으로, KOSPI/KOSDAQ 지수 등락률이 아닙니다.

## 파일 역할

- `main.py`: CLI 인자, 호출 순서, 오류 메시지와 종료 코드.
- `storage.py`: CSV 읽기와 HTML 파일 교체.
- `logic.py`: 행 검증, 등락률·필터·정렬·요약. I/O 없음.
- `report.py`: 외부 텍스트를 escape하여 HTML 문자열 반환. I/O 없음.
- `test_market.py`: 정상·경계·실패·통합 테스트 12개.
- `project-spec.md`: 시나리오, 요구사항, feature, function, test, UML 전체 예제.

입력은 UTF-8 CSV이며 BOM도 허용합니다. 헤더는 `date,code,name,market,previous_close,close,volume` 순서입니다. 한 기준일만 허용하고 종목코드는 중복할 수 없습니다. 종목코드는 선행 0을 보존하는 6자리 문자열, 종가·전일종가는 양의 정수 원, 거래량은 0 이상의 정수 주입니다. 두 종가는 동일한 가격 기준으로 준비되었다고 가정하며 기업행동 조정은 범위 밖입니다.

누락 파일, 잘못된 헤더·행, 날짜 혼합·중복 코드는 오류로 종료하며 기존 보고서를 유지합니다. 헤더만 있는 CSV는 빈 보고서를 만듭니다. 새 HTML은 임시 파일에 완전히 쓴 후 교체합니다. `Report not generated: ...`가 표시되면 브라우저의 기존 보고서는 이전 결과이므로 기준일을 확인합니다. 프로세스 종료 코드는 성공 0, 데이터/파일 오류 1, CLI 사용 오류 2입니다.

## 첨부 문서와 오류 실습 데이터

- [team-name_spec.xlsx](../../labs/session2/team-name_spec.xlsx): 시트별 요구사항·기능·함수·테스트 작성 예시.
- [team-name_user-scenario.md](../../labs/session2/team-name_user-scenario.md): SC-01~03, 아키텍처와 1인 책임 분담.
- `data/invalid-zero.csv`: 전일종가 0인 행을 거부하는 SC-02 입력.
- `data/empty.csv`: 정상 헤더만 있는 SC-03 입력.

워크북의 TEST-01~12는 자동 테스트 실행 결과이며 TEST-13은 브라우저 수동 확인 전까지 Not run이다. 본인 제출물에는 이름·학번과 재실행 결과를 기록한다.
