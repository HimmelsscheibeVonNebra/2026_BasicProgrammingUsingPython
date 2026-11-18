# Sample 2: 한국 주식 분석

Python 3.10 이상과 Flask를 사용합니다. 이 폴더만 복사해도 실행할 수 있습니다.

## 실행

저장소 루트에서:

```bash
cd Sample/sample2
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Windows PowerShell에서는 활성화 명령을 `.venv\Scripts\Activate.ps1`로 바꿉니다.
브라우저에서 http://127.0.0.1:5002 을 엽니다. Ctrl+C로 종료합니다.

## 실습 흐름

1. `data/prices.csv`를 확인합니다. 모든 수치는 2026-11-05 기준 **가상 수업 데이터**입니다.
2. 웹에서 시장을 선택하여 등락률 순위와 상승·하락·보합 수를 비교합니다.
3. CSV의 종가를 바꾸어 다시 조회합니다.
4. 0인 가격이나 중복 코드를 넣고 오류 처리를 확인합니다.

등락률 = (종가 − 전일 종가) / 전일 종가 × 100. 같은 가격 기준을 사용하며,
계산값은 유지하고 화면에서만 소수 둘째 자리로 표시합니다.
평균은 선택된 종목의 동일 가중 표본 평균이며 시장 지수 수익률이 아닙니다.

`app.py`: HTTP 요청과 오류 처리 → `storage.py`: CSV 읽기 → `logic.py`: 검증·분석 → `templates/index.html`: Jinja 렌더링.
Jinja 자동 escaping을 사용하며 종목명에 HTML을 넣어도 실행하지 않습니다.
헤더만 있는 CSV는 유효한 빈 표본(평균 N/A), 파일 누락은 오류입니다.

한국 가격은 정수 원(KRW), 거래량은 정수 주입니다. 005930 같은 코드를 문자열로 유지합니다. ALL 평균 +0.40%, KOSPI +0.33%, KOSDAQ +0.50%입니다.
