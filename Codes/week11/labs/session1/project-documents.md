# Project documents v1

Name:　　　　 Student ID:　　　　 Project:　　　　 Date:

Individual project. Four short documents that describe the same program from four sides. Use one ID scheme everywhere: `REQ-xx` for requirements, `FEAT-xx` for features, function names for contracts, `TEST-xx` for checks. Copy from your week 9 proposal and week 10 design document wherever they already answer a question.

## A. Requirements (12 minutes)

Three to five lines. The statement says what, not how. The check is something a classmate can do at the keyboard in a minute.

| ID | Statement | Priority | Check (input condition, observed result) |
| --- | --- | --- | --- |
| REQ-01 | | Must | |
| REQ-02 | | Must | |
| REQ-03 | | Must | |
| REQ-04 | | Should | |
| REQ-05 | | Could | |

Constraints and quality: Python 3 and the standard library; invalid input is refused with a message; the data file is unchanged after a failure; a missing file does not crash the program.

## B. Feature sheet for F1 (10 minutes)

| Field | FEAT-01 |
| --- | --- |
| Name | |
| Purpose (one sentence) | |
| Basic or extension | basic |
| Usage (command, prompts, allowed values) | |
| Normal flow (numbered steps) | 1.  2.  3. |
| Result the user sees on success | |
| Errors, one per line, each with its message | |
| Serves (REQ IDs) | |

## C. Function contracts (10 minutes)

Copy the functions of F1 from your design document, then add the last two columns.

| Function | Arguments and types | Returns (one type) | Failure behavior | Module | Called by |
| --- | --- | --- | --- | --- | --- |
| | | | | logic.py | main() |
| | | | | | |
| | | | | | |
| | | | | | |

Rules: no `input()`, `print()` or `open()` in logic functions; one return type per function; every failure field filled in.

## D. One UML diagram (10 minutes)

Choose one. Draw it on paper and attach a photo, or write it as text in the box.

- Sequence of `main()` for one normal run: one line per call, `caller -> callee: function(arguments)` then `callee --> caller: what comes back`.
- States of one entry: the states in order, the function that moves the entry from each state to the next, and the rejected branch with its message.

```text

```

## E. Traceability (4 minutes, with a classmate)

Pick one requirement and follow it through all four documents.

| Document | Entry |
| --- | --- |
| Requirement | REQ-0_: |
| Feature | FEAT-0_: |
| Function | |
| UML | |
| Check | TEST-0_: |

Reviewer (feedback only, no shared code):

- Does every requirement have a check a stranger could run? yes / no
- Does the feature sheet list each error with its message? yes / no
- Does every contract state its failure behavior and its module? yes / no
- Strength:
- Concern:
