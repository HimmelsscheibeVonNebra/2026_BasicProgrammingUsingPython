# Week 11 Session 2 lab: ship your F1

Individual work, 30 minutes. You leave with F1 running end to end on a merged pull request.

Before you start: `git status` is clean, `python3 main.py` runs without a traceback, and your design document is open.

Reference: `examples/study_logger_f1/` is the study logger at the end of this lab.

## Step 1: branch and fake (6 minutes)

1. Update and branch:

   ```bash
   git switch main
   git pull
   git switch -c feature/f1-<short-name>     # for example feature/f1-save-entry
   ```

2. In `main.py`, write `main()` for F1 only: ask for F1's inputs, call F1's functions by their design names, print the result. Keep the `try`/`except ValueError` from week 10's main.
3. Every function `main()` calls must exist. Give the ones you have not written a fake body: `return` a constant with the right shape (a dict, a list, a string). Leave the docstring alone.
4. Run `python3 main.py`. It must finish without a traceback. Wrong output is fine for now.
5. Commit: `git add -A && git commit -m "Wire main for F1 with fakes"`

## Step 2: replace the fakes (14 minutes)

Core first: logic, then storage, then report. One function per loop.

1. Read the docstring. Write the simplest body that keeps the promise.
2. For a logic function, add one check to `test_logic.py`: the good case as an `assert`, the bad cases in a `try` that must raise `ValueError`.
3. Run both:

   ```bash
   python3 test_logic.py     # All checks passed.
   python3 main.py           # does the F1 job for real
   ```

4. Commit: `git add -A && git commit -m "Implement <function name>"`
5. Next fake. Stop when no fake is left on F1's path.

Rules: no `input()`, `print()` or `open()` in `logic.py`. Do not start F2 or F3. If a function is shared between features, implement only what F1 needs today.

Stuck for more than three minutes on how a library works? Write a ten-line spike in `scratch/` (ignored by Git), get the answer, delete it.

## Step 3: tidy, push, pull request (8 minutes)

1. Refactor hat: names from the design document, one constant for the data file path, no dead branches. Run the checks, then commit: `git commit -am "Refactor: <what you changed>"`
2. `git push -u origin feature/f1-<short-name>`
3. On GitHub: **Compare & pull request**. Description:

   ```text
   ## What
   ## Why
   ## How I checked
   ## Not in this PR
   ```

4. Self-review on the **Files changed** tab:
   - [ ] `python3 test_logic.py` prints `All checks passed.`
   - [ ] `python3 main.py` does the F1 job; a bad entry prints `Not saved` and changes nothing
   - [ ] No `input()`, `print()` or `open()` in `logic.py`
   - [ ] No fake body left on F1's path; no leftover debug `print()`
   - [ ] Only F1 in this pull request
5. **Merge pull request**, **Delete branch**, then on your laptop:

   ```bash
   git switch main
   git pull
   git log --oneline
   ```

## Submit via the LMS

1. Link to the merged pull request (or the open one, if you ran out of time; finish before next session)
2. The output of `git log --oneline` (paste as text)

## When it does not run

| Message | Cause | Fix |
| --- | --- | --- |
| `ModuleNotFoundError: No module named 'logic'` | Wrong folder | `cd` into the project folder, then `python3 main.py` |
| `NotImplementedError: make_record` | A stub is still on F1's path | That function is your next loop |
| `TypeError: can only concatenate str (not "int")` | A value is still text | Convert once with `int()`, inside logic |
| `FileNotFoundError: 'data/study.csv'` | The `data/` folder is missing | `mkdir data`, then run again |
| Nothing printed, no error | `main()` is never called | Add `if __name__ == "__main__": main()` to `main.py` |
| `AssertionError` in `test_logic.py` | The body breaks the contract | Read the failing line; fix the body, not the check |
