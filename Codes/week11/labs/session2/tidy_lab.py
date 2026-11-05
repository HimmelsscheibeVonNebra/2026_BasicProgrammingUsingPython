"""Practice 2: refactor without changing behavior.

Everything below works: every check at the bottom prints PASS. The code is
still hard to read. The names say nothing, the number 2000 appears three
times, and the same line is written twice.

Your task (8 minutes): make it readable without changing any output.

  Move 1  Rename: entries, day, ml, totals instead of x, d, m, tmp.
  Move 2  Constant: 2000 means "daily goal in ml". Name it once, at the top.
  Move 3  Extract: the line that builds "day: total ml (status)" exists
          twice. Write it once as a function and call it.
  Bonus   Guard clause: goal_status does not need a nested if.

Run the file after every move. All six checks must still print PASS.
Keep the function names used by the checks. Do not change the check() calls.
"""


def daily_totals(x):
    """Return {day: total ml} for a list of (day, ml) pairs. An empty list returns {}."""
    tmp = {}
    for d, m in x:
        if d in tmp:
            tmp[d] = tmp[d] + m
        else:
            tmp[d] = m
    return tmp


def goal_status(x):
    """Return "goal" if x ml reaches the daily goal of 2000 ml, otherwise "under"."""
    if x >= 2000:
        return "goal"
    else:
        if x < 2000:
            return "under"


def format_report(x):
    """Return one line per day in day order, like "2026-11-10: 2100 ml (goal)"."""
    tmp = daily_totals(x)
    out = []
    for d in sorted(tmp):
        if tmp[d] >= 2000:
            out.append(d + ": " + str(tmp[d]) + " ml (" + goal_status(tmp[d]) + ")")
        else:
            out.append(d + ": " + str(tmp[d]) + " ml (" + goal_status(tmp[d]) + ")")
    return out


def check(name, actual, expected):
    if actual == expected:
        print("PASS", name)
    else:
        print("FAIL", name, "-> got", repr(actual), "expected", repr(expected))


if __name__ == "__main__":
    sample = [("2026-11-10", 500), ("2026-11-10", 1600), ("2026-11-11", 1500)]
    check("daily_totals(sample)", daily_totals(sample),
          {"2026-11-10": 2100, "2026-11-11": 1500})
    check("daily_totals([])", daily_totals([]), {})
    check("goal_status(2100)", goal_status(2100), "goal")
    check("goal_status(1500)", goal_status(1500), "under")
    check("format_report(sample)", format_report(sample),
          ["2026-11-10: 2100 ml (goal)", "2026-11-11: 1500 ml (under)"])
    check("format_report([])", format_report([]), [])
