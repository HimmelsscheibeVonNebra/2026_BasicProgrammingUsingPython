# 11주차 — 프로토타이핑과 MVP (1인 프로젝트)

1차는 텀프로젝트 문서 네 가지(Requirement, Feature, Function, UML)를 쓰는 법을 다루고, 2차는 10주차의 설계 문서와 저장소 골격을 실행되는 코드로 바꾼다(Must 기능 F1을 얇은 수직 조각으로 끝까지 실행하고 merge된 Pull Request로 남긴다). 강의계획서의 "프로토타이핑, 코드 구조화·리팩토링 원칙 / 핵심 기능 1차 구현(MVP)"을 1인 프로젝트 방침에 맞춰 **기능 하나 = 브랜치 하나 = PR 하나**로 운영한다. 예시는 9·10주차의 공부 시간 기록기(`study.csv`: `date,course,minutes`)를 그대로 잇는다. 모든 자료는 영어이며 각 120분이다.

## 1차 — Writing the Project Documents (24장)

[PDF](week11-session1.pdf) · [PPTX](week11-session1.pptx) · [ODP](week11-session1.odp) · [슬라이드 원본](week11-session1.md) · [영어 말하기 대본](week11-session1-speaking-script-en.md) · [실습 양식](labs/session1/project-documents.md)

리눅스 시스템프로그래밍 과목의 `output/term-project/term-project-documents-v02.pptx`(한국어 21장)를 영어로 옮긴 덱이다. 원본 21장의 순서와 내용을 그대로 유지하되, 예시를 C/Linux 자원 제한 명령 실행기에서 이 과목의 파이썬 공부 시간 기록기로 바꿨다(REQ·FEAT·TEST ID 체계와 다이어그램 종류는 동일). 원본 1–15장은 1–15장에, 16–21장은 17–22장에 대응하고, 휴식(16)·실습(23)·제출(24) 세 장을 더해 120분 수업으로 맞췄다.

| 시간 | 내용 | 슬라이드 |
|---|---|---|
| 000–014 | 오프닝: 문서의 범위, 네 문서의 역할, 요구사항과 구현의 연결, 공통 예제 | 1–5 |
| 014–022 | Doc 1 Requirement: 명세 구성, 작성 예시, 요구사항과 검증의 대응 | 6–8 |
| 022–030 | Doc 2 Feature: 명세 구성, 작성 예시(F1), 정상 흐름과 오류 흐름 | 9–11 |
| 030–040 | Doc 3 Function: 함수 설계, make_record() 예시, 함수 분해, 함수와 모듈의 책임 | 12–15 |
| 040–050 | 휴식 | 16 |
| 050–066 | Doc 4 UML: 다이어그램 선택, 유스케이스·시퀀스·상태 예시, 문서 사이의 추적, 문서 검토 | 17–22 |
| 066–112 | 실습: 내 프로젝트의 네 문서 (A 요구사항 12분, B 기능 시트 10분, C 함수 계약 10분, D UML 10분, 동료 추적 4분) | 23 |
| 112–120 | 제출, 다음 수업 예고 | 24 |

제출물은 [project-documents.md](labs/session1/project-documents.md) 한 파일이다. 요구사항 표(ID·문장·우선순위·검증), F1 기능 시트, 함수 계약 표(10주차 설계 문서에서 복사하고 모듈·실패 정책을 추가), UML 한 장(시퀀스 또는 상태, 텍스트나 사진), 추적 표와 동료 검토로 구성된다.

## 2차 — From Design to Running Code (39장)

[PDF](week11-session2.pdf) · [PPTX](week11-session2.pptx) · [ODP](week11-session2.odp) · [슬라이드 원본](week11-session2.md) · [영어 말하기 대본](week11-session2-speaking-script-en.md) · [학생 배포 ZIP](week11-session2-code.zip)

| 시간 | 내용 | 슬라이드 |
|---|---|---|
| 000–013 | 오프닝, 저장소 점검, 레이어 대 슬라이스 | 1–5 |
| 013–033 | Act 1 Prototype: MVP의 세 가지 뜻, 슬라이스, 가짜(fake)로 먼저 돌리기, 하나씩 교체, 스파이크, work·right·fast, 연습 1 | 6–13 |
| 033–052 | Act 2 Structure: 스텁에서 본문으로, storage, F1만 배선한 main, 경계를 새는 지름길(TRAP), 실행 후 커밋, 테스트 키우기, 완료 기준 | 14–21 |
| 052–062 | 휴식 | 22 |
| 062–082 | Act 3 Refactor: 두 개의 모자, 냄새 5·이동 5, before/after, 가드 절, 중복 제거, 눈 감고 리팩터링(TRAP), 연습 2 | 23–31 |
| 082–112 | 실습: F1 배송 — 오류 대처표, 브랜치·가짜, 가짜 교체, 정리·push·PR | 32–36 |
| 112–120 | 흔한 실수, 확인 질문, 제출 | 37–39 |

| 실습 | 학생용 | 교수용 |
|---|---|---|
| 연습 1: 내 F1 슬라이스 그리기 (4분, 종이) | 슬라이드 13 | — |
| 연습 2: 동작을 바꾸지 않는 리팩터링 (8분) | [tidy_lab.py](labs/session2/tidy_lab.py) | [정답](instructor/solutions/tidy_lab.py) |
| 실습: F1 슬라이스 (30분, 제출) | [slice-lab.md](labs/session2/slice-lab.md) | — |
| 참고 예제: 2차 시작 상태 (계약만 있는 스텁) | [examples/study_logger_skeleton/](examples/study_logger_skeleton/) | — |
| 참고 예제: 2차 종료 상태 (F1 완료) | [examples/study_logger_f1/](examples/study_logger_f1/) | — |
| 교수 시연: F1 커밋 5개 재현 | — | [slice_demo.sh](instructor/slice_demo.sh) |

연습 2의 `tidy_lab.py`는 처음부터 PASS 6개를 출력한다. 학생은 이름 바꾸기, 상수 추출, 함수 추출(보너스: 가드 절)을 적용하면서 출력이 한 글자도 바뀌지 않게 유지한다. 실습 제출물은 merge된 PR 링크(미완성이면 열린 PR 링크)와 `git log --oneline` 출력이다. 슬라이드 19의 커밋 해시는 모두 실제 출력이며 `bash instructor/slice_demo.sh`가 이름과 날짜를 고정해 같은 해시를 다시 만든다(`.build/slice_demo_output.txt`).

F2(파일 다시 읽기)·F3(주간 합계) 슬라이스와 네 파일 전체의 리팩터링 패스, MVP 시연은 다음 수업 몫이다. `python3 main.py`가 Must 기능 전부를 처음부터 끝까지 수행하면 MVP 마감 통과다.

## 제작과 검증

- 원본: `week11-session1.md`, `week11-session2.md`. 10주차 문법(`<!-- section N -->`, `> LABEL: ...`, ```` ```text ````, ```` ```bash ````)에 두 가지를 더했다. 리팩터링 슬라이드용 ```` ```before ````·```` ```after ```` 코드 상자(빨강 BEFORE·초록 AFTER 탭)와, 구분 슬라이드 없이 오른쪽 위 칩만 바꾸는 `<!-- act N -->` 표시. 1차 덱은 칩 머리말을 ACT 대신 DOC으로 쓴다(`render_pdf.py`의 `kicker`).
- 그림 21장: `/usr/bin/python3 .build/make_figures.py` → `figures/`
- 덱: `/usr/bin/python3 .build/render_pdf.py week11-session1` (session2도 같음). PDF와 ODP를 만들고, 각 슬라이드 발표자 노트에 말하기 대본의 해당 절을 넣는다. `--draft`를 붙이면 대본 없이 PDF만 만들고 넘치는 슬라이드를 한 번에 모두 나열한다. PPTX는 LibreOffice로 변환한다: `/Applications/LibreOffice.app/Contents/MacOS/soffice --headless --convert-to pptx week11-session1.odp`
- 검증: `/usr/bin/python3 .build/verify_materials.py`. 두 덱의 슬라이드·대본 순서와 시간 합 120분, 슬라이드의 모든 Python·BEFORE·AFTER 블록 실행과 OUTPUT 상자 일치(BEFORE와 AFTER는 같은 출력), 두 예제 폴더 실행, 연습 2 스타터·정답, Git 시연 해시, 1차 실습 양식의 구성, ODP·PPTX 장수와 노트, 학생 ZIP 구성을 확인한다.
- 렌더러는 10주차 것을 바탕으로 한다. OUTPUT 상자가 오른쪽 열에 들어가는지 판단할 때 상자 아래 여백을 빠뜨리던 문제를 고쳤고, 제목이 오른쪽 위 칩과 겹치면 실패하는 검사를 추가했다.
