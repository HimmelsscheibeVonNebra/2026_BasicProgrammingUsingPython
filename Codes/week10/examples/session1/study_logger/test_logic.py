"""Acceptance criteria from the week 9 proposal, written as checks."""
from logic import make_record, parse_minutes, weekly_totals

sample = [make_record("2026-10-24", "python", "90"),
          make_record("2026-10-25", "Stats ", "45")]
assert weekly_totals(sample) == {"python": 90, "stats": 45}
assert weekly_totals([]) == {}
for bad in ["-30", "0", "abc"]:
    try:
        parse_minutes(bad)
    except ValueError:
        pass
    else:
        raise AssertionError(f"{bad!r} was accepted")
print("All checks passed.")
