# Week 11 Session 1 — Writing the Project Documents: speaking script

24 slides, 120 minutes including a 10-minute break. One section per slide, in deck order; the renderer copies each section into that slide's speaker notes. Minute ranges are elapsed time from the start of class.

Labels: **Say** is ready-to-read English. **Do** is a private action. **Ask** is a question for students; **Answer** is the expected answer, revealed after they try. **Next** is the transition.

## Slide 1 — Writing the Project Documents
- **Time:** 00–02 (2 min)
- **Say:** You have a proposal from week 9 and a design document from week 10. Today we put the project on paper in a form other people can check: four short documents, each answering one question about the same program. Requirement, feature, function, UML. The second half is a lab where you write them for your own project.
- **Do:** Have the week 10 design document template open in a second window; you will point at it in the Function part.
- **Next:** First, what these documents are for.

## Slide 2 — Project Guidance and Document Scope
- **Time:** 02–05 (3 min)
- **Say:** The project is a Python 3 program, standard library only, that keeps data in a file and reports on it. Every project shares the same checks: bad input, a missing or malformed file, and a file that stays unchanged after a failure. The documents explain the problem, the feature scope, the module structure and the data format.
- **Say:** One caveat before we start: the four documents on these slides are a writing guide. Which ones you submit, and their weight, follows the syllabus and the LMS. The lab template today is the submission for this session.
- **Do:** Point at the timeline. The break is at minute 40; the lab starts at minute 66.
- **Next:** The four questions.

## Slide 3 — The Role of the Four Documents
- **Time:** 05–08 (3 min)
- **Say:** Four questions about one program. What must hold? That is the requirement, with a pass/fail criterion. What does the user do? That is the feature: how to use it and what they observe. Which Python function does it? That is the function contract: inputs, return value, failure. How does it all connect? That is UML: modules, the order of calls, state changes.
- **Ask:** Which of these four did you already write in week 10?
- **Answer:** Function contracts and the module map. Today adds requirements and features above them and UML beside them.
- **Next:** How the four connect.

## Slide 4 — Linking Requirements to Implementation
- **Time:** 08–11 (3 min)
- **Say:** Read the chain left to right. A requirement is a condition to satisfy. A feature is what the user does to satisfy it. A function is the code's promise. A check decides whether the promise holds. UML sits under feature and function and shows the structure and flow that connect them.
- **Say:** The rule that makes this work: the same ID in every document. REQ-02 in the requirements, REQ-02 in the feature sheet, REQ-02 next to the function, REQ-02 in the test. Then anyone can trace a requirement to its code and its check.
- **Next:** One example for everything today.

## Slide 5 — Shared Example: The Study Logger
- **Time:** 11–14 (3 min)
- **Say:** The study logger from weeks 9 and 10, so that every document today has a concrete line in it. Three basic features: log one entry, reload entries from the file, show weekly totals per course. The result is one line per course, largest first, or "Not saved" with a reason. The shared responsibilities: reject bad input, keep the file unchanged on failure, survive a missing file.
- **Say:** Minutes are what the student types. A program that measures time with a clock is a different, extension feature. Keep that distinction; it decides what is in scope.
- **Next:** Document one.

## Slide 6 — Requirement: The Specification
- **Time:** 14–17 (3 min)
- **Say:** A requirements specification has four parts. Purpose and scope: who has the problem, what the program solves, where it stops. Requirement items: each with an ID, a statement, a priority and a check. Functional requirements: the things the program does. Constraints and quality: the environment, input validation, the file unchanged on failure.
- **Say:** Look at the row format on the right. One line, one condition. The check is something a classmate can do at the keyboard.
- **Next:** The example rows.

## Slide 7 — Requirement Example
- **Time:** 17–20 (3 min)
- **Say:** Four requirements for the study logger. Each says what, not how: no function names, no file formats. Each has a check that takes a minute at the keyboard. REQ-01: type a valid entry, one new row appears. REQ-02: type minus thirty, "Not saved", the file unchanged. REQ-03: two python entries and one stats entry, python first with the sum. REQ-04: run twice, the second run counts the first.
- **Say:** Must requirements are the MVP. Should and Could wait until the MVP runs. These checks become test_logic.py next session and the test list in week 12.
- **Next:** What makes a check a check.

## Slide 8 — Matching Requirements to Checks
- **Time:** 20–22 (2 min)
- **Say:** A check has two halves. The input condition: exactly what is typed, or what the file holds before the run. The observed result: what is printed, and what the file contains afterwards. If the author has to stand next to the grader and explain, it is not a check yet.
- **Ask:** REQ-04 says "entries survive a restart." What is the input condition?
- **Answer:** Run the program twice, with one entry in the first run. The observed result: the second run's totals include it.
- **Next:** Document two: the feature.

## Slide 9 — Feature: The User-Facing Specification
- **Time:** 22–25 (3 min)
- **Say:** A feature is the program as the user meets it. Identification: an ID, a name, a purpose, basic or extension. How to use: the command, the prompts, the allowed values, what must be true before the run. Behavior and result: the normal flow and the output the user checks. Exceptions and links: bad input, failures, and the requirement IDs this feature serves.
- **Say:** The sheet on the right is the skeleton. Seven lines. You will fill one in the lab.
- **Next:** Filled in for F1.

## Slide 10 — Feature Example: Logging One Entry
- **Time:** 25–28 (3 min)
- **Say:** FEAT-01, log one entry, basic. Usage: python3 main.py, then three prompts. Flow: check the input, build the record, append one row. Result: "Saved." Errors, one by one, each with its message: bad minutes or an empty course gives "Not saved" with the reason and an unchanged file; a missing data folder is reported and nothing is written. Serves REQ-01, 02 and 04.
- **Say:** The usage line is what the demo will type in week 16. Write it so that a stranger could. And "handles errors" is not a line; each error is a line.
- **Next:** The two paths through a feature.

## Slide 11 — A Feature's Normal Path and Error Path
- **Time:** 28–30 (2 min)
- **Say:** The good day and the bad day both belong in the sheet. The normal path: four steps, each with something the user can observe. The input error: a sentence with the reason, nothing written. The file error: the cause reported, nothing half-written, the program ends cleanly.
- **Next:** Document three: the function.

## Slide 12 — Function: Python Function Design
- **Time:** 30–33 (3 min)
- **Say:** In this course, Function means one Python function with a contract, and your week 10 design document already has the fields. Signature: name, parameters with types, return type. Inputs and results: allowed values and units, what success returns, how failure shows. Where it runs: the module, the caller, and whether it touches the keyboard or a file. Failure and resources: raise or return None, and who opens and closes the file.
- **Do:** Show the contract table in the week 10 design document template and point at the matching columns.
- **Next:** One function, fully written.

## Slide 13 — Function Example: make_record()
- **Time:** 33–36 (3 min)
- **Say:** The contract lives in the docstring, the body under it, and one call shows the promise kept. Input: three strings straight from input(); the course is trimmed and lower-cased here and nowhere else. It is called by main before anything is written, and returns one dict with minutes as an int. Failure: a ValueError with a reason; main prints "Not saved" and writes nothing.
- **Ask:** Why does the docstring mention "above 0" and not "positive"?
- **Answer:** Because "positive" is ambiguous about zero. A check for zero is in REQ-02's test. Contracts say the boundary.
- **Next:** All six functions.

## Slide 14 — Decomposing into Functions
- **Time:** 36–38 (2 min)
- **Say:** Six functions, six single responsibilities, named by the verb test from week 10. Two rule functions, two file functions, one report function, and main that calls them. Each line here is one row of your contract table. If a function needs "and" to describe it, split it before you write the contract.
- **Next:** Where they live.

## Slide 15 — Functions and Modules: Who Does What
- **Time:** 38–40 (2 min)
- **Say:** After main asks, each module answers one kind of question, and none of them asks the user anything. main.py asks, calls and prints and holds no rules. logic.py holds the rules and never touches the keyboard or the disk. storage.py is the only module that opens the file. report.py turns results into lines. This is the week 10 module map; UML will draw it.
- **Next:** Break.

## Slide 16 — Halftime
- **Time:** 40–50 (10 min)
- **Say:** Ten minutes. Three documents down, one to go. After the break: UML and the traceability chain, then the lab.
- **Do:** Hand out or post the lab template link: labs/session1/project-documents.md.

## Slide 17 — UML: Choosing a Diagram by Purpose
- **Time:** 50–53 (3 min)
- **Say:** You do not need every diagram. Pick the one that answers your reader's question. Who uses it and for what: a use case diagram. Which file imports which: a module diagram. In what order are calls made: a sequence diagram. What happens to one entry: a state diagram, or an activity diagram for steps with error branches.
- **Say:** In a Python project the module structure and the order of calls in main are the things worth drawing. Those two diagrams usually answer every question a grader has.
- **Next:** Use case.

## Slide 18 — UML Use Case Example
- **Time:** 53–55 (2 min)
- **Say:** One actor, the student. One system boundary, the study logger. Three goals: log an entry, review weekly totals, find earlier entries again. Goals, not functions. Function names do not appear here; the order of calls belongs in the sequence diagram.
- **Next:** Sequence.

## Slide 19 — UML Sequence Example: One Run
- **Time:** 55–58 (3 min)
- **Say:** One run, the normal path, time flowing downward. Every solid arrow is a call from your contract table; every dashed arrow is a return carrying one data shape: a record, a list of records, a totals dict, lines. main calls logic first, so nothing is written before the record is valid.
- **Say:** The failure path, the ValueError, is a separate branch or a second, shorter diagram. Do not draw both on one sheet.
- **Next:** State.

## Slide 20 — UML State Example: One Entry
- **Time:** 58–60 (2 min)
- **Say:** Four states and one dead end. Typed, then checked by make_record, saved by append_record, counted by weekly_totals. Rejected: an empty course or bad minutes ends the entry with "Not saved", and nothing is written. A file error after the check is also reported, and nothing is half-written.
- **Next:** The chain through all five.

## Slide 21 — Traceability Across Documents
- **Time:** 60–63 (3 min)
- **Say:** Follow REQ-02 down the chain. The requirement says minutes that are not positive are rejected. FEAT-01 shows it to the user: typing minus thirty gives "Not saved". parse_minutes enforces it in logic.py by raising ValueError. The state diagram draws it as the rejected branch. TEST-02 proves it: parse_minutes of minus thirty must raise. Write the ID in every document and a grader, or you in week 14, can follow the chain in either direction.
- **Next:** Five questions before you call the documents done.

## Slide 22 — Document Review and Demo Preparation
- **Time:** 63–66 (3 min)
- **Say:** Scope: are basic and extension features separated, and is the MVP line visible? Completion: can each requirement be judged pass or fail with its check? Consistency: do the feature sheet, the function contracts and the UML flow agree? Data checks: bad input, a missing file, the header row, the file unchanged on failure. Reproduction: the setup, the run command, one normal and one error scenario, written down.
- **Say:** These five are the review questions in the lab's last four minutes.
- **Next:** The lab.

## Slide 23 — Lab: Your Four Documents
- **Time:** 66–112 (46 min)
- **Say:** Forty-six minutes. Open labs slash session1 slash project-documents.md. Part A, twelve minutes: three to five requirements, each with a check. Part B, ten minutes: the feature sheet for your F1. Part C, ten minutes: your function contracts, copied from the design document, with the module and the failure policy added. Part D, ten minutes: one UML diagram, a sequence of main or the states of one entry, on paper or as text. Last four minutes: swap with a classmate and trace one REQ ID through all four documents.
- **Do:** Circulate. Common gaps: a requirement with no check, a feature sheet with "handles errors" as one line, a contract with no failure field. Keep the five review questions on the projector during the last four minutes.
- **Ask:** At the end, ask two students to read their REQ-02 chain aloud, requirement to test.
- **Answer:** A good chain names the same ID five times and a function from the contract table.
- **Next:** Submission.

## Slide 24 — Submit and Next Session
- **Time:** 112–120 (8 min)
- **Say:** Submit project-documents.md via the LMS today. Keep your REQ and FEAT IDs; they go into commit messages, test names and the README from now on. Next session: From Design to Running Code. Your F1 runs end to end on a feature branch, so bring a laptop where your repository is cloned, git status is clean and python3 main.py runs.
- **Say:** Must scope stays frozen. A new idea becomes a Should or Could line, not a new Must requirement.
- **Do:** Use the remaining minutes for questions on the documents, and for anyone whose repository does not run yet.
