# 12주차 2차 — 짧은 실험 활동지

이름 / 짝:

모든 명령은 저장소 루트에서 실행한다. Python 표준 라이브러리만 사용한다. 실험 코드는 11주차 MVP를 읽어 사용하며 파일 실험은 임시 폴더에서만 실행한다. 개인 기능 확장은 예제 복사본이나 개인 저장소에서 진행한다.

## A. 입력 판정 투표 (5분, 개인 후 짝 토론)

**실행 전에** 각 값을 허용/거절로 판정한다. 계약은 “최소 거래량은 bool을 제외한 0 이상의 int”다. CLI 문자열 파싱과 함수에 직접 전달하는 값은 구분한다.

| 값 | 내 예상 | 짝의 예상 | 실행 결과와 이유 |
|---|---|---|---|
| 0 | | | |
| 100 | | | |
| -1 | | | |
| True | | | |
| "100" | | | |
| 1.5 | | | |

```bash
python3 12week/examples/validation_lab/playground.py verdict
```

설명할 질문: `isinstance(True, int)`만 확인하면 어떤 문제가 생길까?

## B. CSV 고장 실험 (10분, 짝 실습)

한 명은 예측을 기록하고 한 명은 실행한다. 새 사례를 추가할 때 역할을 바꾼다. 혼자라면 예상 열을 먼저 채운 뒤 실행한다.

| 사례 | 예상 반환 코드 / OLD 보존 여부 | 실제 결과 / 오류 원인 |
|---|---|---|
| 정상 CSV | | |
| 헤더만 있는 CSV | | |
| 존재하지 않는 파일 | | |
| 음수 거래량 | | |
| 내가 추가한 사례: | | |

```bash
python3 12week/examples/validation_lab/playground.py csv
```

`csv_experiment()`의 `cases`에 잘못된 날짜 또는 필수 열 누락 사례를 추가한다. 한 번에 한 가지 조건만 바꾼다. 메시지뿐 아니라 반환 코드와 출력 파일 상태를 함께 기록한다.

완료 증거: 정상 빈 결과가 OLD를 교체하는 이유와 오류가 OLD를 보존하는 이유를 각각 한 문장으로 적는다.

## C. 보고서 구출 실험 (8분, 관찰을 테스트로 바꾸기)

```bash
python3 12week/examples/validation_lab/playground.py rescue
```

예상: 예외는 ______ / 기존 출력은 ______ / 남은 파일은 ______

실제: 예외는 ______ / 기존 출력은 ______ / 남은 파일은 ______

`rescue()`의 임시 폴더 설정을 참고해 `unittest.TestCase`의 테스트 메서드 하나를 작성한다. 기존 테스트 복사본에 추가하거나 아래 뼈대를 별도 `test_rescue.py`로 저장한다. 별도 파일은 `playground.py` 옆에 둔다.

```python
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
from playground import write_html

class RescueTests(unittest.TestCase):
    def test_failed_replace(self):
        with TemporaryDirectory() as folder:
            output = Path(folder) / "index.html"
            output.write_text("OLD", encoding="utf-8")
            with patch("storage.os.replace", side_effect=OSError("disk")):
                # TODO: assertRaises 안에서 write_html(output, "NEW") 호출
                pass
            # TODO: assertEqual로 OLD 보존과 남은 파일 목록 검사
```

```bash
python3 -m unittest discover -s 12week/examples/validation_lab -p 'test_rescue.py' -v
```

완료 기준: 세 가지 검사를 모두 작성하고 테스트가 실제로 실행됐는지 확인한다. 고급 과제는 복사본에서 `write_html`을 `Path(path).write_text(...)`로 바꾼 뒤 같은 테스트가 결함을 잡는지 확인하는 것이다.

## D. 테스트로 결함 잡기 (8분, 입력 교환)

계약: 기준 이상 포함, bool 거절, 필터 전에 전체 중복 검증.

| 잘못된 구현 후보 | 결함을 드러내는 최소 입력 | 올바른 기대 결과 |
|---|---|---|
| A: `volume > threshold` | | |
| B: `isinstance(value, int)`만 검사 | | |
| C: 필터 후 중복 검사 | | |

짝에게 후보 이름을 가리고 입력만 보여준다. 짝은 어떤 후보를 잡을 수 있는지 설명한다. 혼자라면 각 입력을 올바른 구현과 후보 구현에 손으로 적용한다.

중복 사례는 같은 날짜·코드를 가진 두 행 중 하나만 기준 이상이 되도록 만든다. 행마다 다른 코드로 만들면 중복 검증 결함을 잡을 수 없다.

완료 증거: 표에서 두 사례 이상을 [프로젝트 테스트 계획](project-review.md)에 옮긴다.

## E. 90초 사용자 시연 (결과 시연 10분 안에서 진행)

- 30초: 사용자가 정상 보고서에서 시장·종목 수·순위를 설명한다.
- 30초: 빈 보고서의 안내가 충분한지 사용자가 말한다.
- 30초: 구현자가 새 필터 테스트를 실행하고 기준과 같은 값의 포함 여부를 보여준다.

관찰한 문제 또는 확인한 수락 기준:

CLI 확장이 없으면 기존 main 보고서와 새 함수 테스트를 각각 보여준다. 함수 확장이 자동으로 CLI 보고서에 적용된다고 설명하지 않는다.

## 리뷰와 퇴실 질문

리뷰 의견은 “입력 ___ 에서 기대 ___, 실제 ___, 근거 테스트 ___” 형식으로 하나 이상 기록한다. 동료가 없으면 자신의 diff에서 반례를 찾는다.

1. 실패와 빈 결과를 구별한 실행 증거는?
2. 내가 작성한 테스트가 잡는 구체적인 결함은?
3. 필터로 숨겨지는 중복 코드도 거절해야 하는 이유는?

최종 제출은 [프로젝트 리뷰 양식](project-review.md)에 활동 증거를 연결한다. 활동지는 짧은 메모로 제출해도 된다.
