"""Acceptance criteria for F1, written as checks. Grows with every logic function."""
from logic import make_record, parse_minutes

assert parse_minutes("90") == 90
rec = make_record("2026-11-10", " Python ", "30")
assert rec == {"date": "2026-11-10", "course": "python", "minutes": 30}
for bad in [("2026-11-10", "", "30"), ("2026-11-10", "python", "-30"),
            ("2026-11-10", "python", "abc")]:
    try:
        make_record(*bad)
    except ValueError:
        pass
    else:
        raise AssertionError(f"{bad} was accepted")
print("All checks passed.")
