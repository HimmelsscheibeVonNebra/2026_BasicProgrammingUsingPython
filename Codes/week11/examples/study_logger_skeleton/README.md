# Study logger

For a student who takes several courses, my program records study sessions and shows where the week went.

## Status

Week 10: design and skeleton. Every function has its contract as a docstring; the bodies are TODO.

## Setup

```bash
python3 --version   # 3.9 or newer
python3 main.py
```

## Files

| File | Responsibility |
| --- | --- |
| main.py | Runs the program: asks, calls, prints |
| logic.py | Rules and calculations; no input, print or open |
| storage.py | Reads and writes files in data/ |
| report.py | Turns results into text lines |
| data/study.csv | date,course,minutes; two rows checked by hand |
