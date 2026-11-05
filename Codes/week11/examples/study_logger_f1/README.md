# Study logger

For a student who takes several courses, my program records study sessions and shows where the week went.

## Status

Week 11, session 2: F1 runs end to end. `python3 main.py` asks for date, course and minutes and appends a valid entry to `data/study.csv`. F2 (reload) and F3 (weekly totals) are stubs until next session.

## Setup

```bash
python3 --version   # 3.9 or newer
python3 test_logic.py   # All checks passed.
python3 main.py
```

## Files

| File | Responsibility |
| --- | --- |
| main.py | Runs the program: asks, calls, prints |
| logic.py | Rules and calculations; no input, print or open |
| storage.py | Reads and writes files in data/ |
| report.py | Turns results into text lines |
| test_logic.py | Acceptance checks for the logic functions |
| data/study.csv | date,course,minutes; two rows checked by hand |
