# Week 11 Session 2 — From Design to Running Code: speaking script

39 slides, 120 minutes including a 10-minute break. One section per slide, in deck order; the renderer copies each section into that slide's speaker notes. Minute ranges are elapsed time from the start of class.

Labels: **Say** is ready-to-read English. **Do** is a private action. **Ask** is a question for students; **Answer** is the expected answer, revealed after they try. **Next** is the transition.

## Slide 1 — From Design to Running Code
- **Time:** 00–01 (1 min)
- **Say:** Two weeks ago you wrote a proposal. Last week you turned it into a design and gave it a repository. Every function exists, with a contract, and almost none of them do anything. Today that changes. By the end of the lab your first Must feature runs, start to finish, on a merged pull request.
- **Do:** Have the week 10 design document template and a student-style skeleton repository open in VS Code on the projector.
- **Next:** Here is how the two hours run.

## Slide 2 — The Plan: Run Something Today
- **Time:** 01–03 (2 min)
- **Say:** Three acts and a lab. Act one is about prototyping: the thinnest version that runs end to end, with fakes where the real code is missing. Act two is about structure: filling the skeleton one contract at a time without breaking the week 10 shape. Act three is refactoring: changing the shape of code without changing what it does. The last half hour is your own F1.
- **Do:** Point at the timeline. The break is at minute 52.
- **Next:** Where does today sit in the project?

## Slide 3 — Where We Are in the Project
- **Time:** 03–05 (2 min)
- **Say:** Week 10 left you a skeleton. Week 12 is tests and debugging, which need a program that already runs. Week 11 is the week it starts running. Today: F1. Next session: F2, F3 and a refactor pass. At the end of next session the MVP is due: every Must feature, thinnest version, from python3 main.py.
- **Say:** Not "almost running". Running. That is the rule on this slide.
- **Next:** Before we build on the skeleton, check it.

## Slide 4 — Check Your Repository First
- **Time:** 05–10 (5 min)
- **Say:** Five minutes. Open a terminal in your project folder and go down the list. Pull first, so your laptop has the merged pull request from week 10. Then status, then run main. Then open each module and check that every function from your design document has a stub with the contract as its docstring.
- **Do:** Walk the room. The common gaps: a function in the design table with no stub, and a main.py that crashes because an import name does not match.
- **Ask:** Who has a function in the design document that does not exist in the code yet?
- **Answer:** Add the stub now: def with the docstring and raise NotImplementedError. That is a legal body and the lab needs it.
- **Next:** Now, why prototype at all? Two students, same design.

## Slide 5 — Two Ways to Spend Week 11
- **Time:** 10–13 (3 min)
- **Say:** Student A works in layers: finish storage.py completely, then logic.py, then report.py, then main.py. Nothing runs until Thursday night, and then everything that is wrong is wrong at once, in two hundred lines. Student B works in slices: F1 through every file on Monday, ugly but running. F2 Tuesday. F3 Wednesday. Refactor Thursday. Demo Friday.
- **Ask:** Both students have the csv header bug. Who finds it first, and how long do they search?
- **Answer:** B finds it on Monday, in the twelve lines of append_record. A finds it on Thursday, somewhere in two hundred lines, along with every other bug.
- **Next:** Act one: prototype.

## Slide 6 — Prototype: Make It Run First
- **Time:** 13–14 (1 min)
- **Say:** A program that runs badly teaches you more than a design that sits perfectly. In this act: what MVP means for your project, what it leaves out, and how to fake the parts you do not have so the whole pipeline runs today.
- **Next:** Three words.

## Slide 7 — What MVP Means Here
- **Time:** 14–17 (3 min)
- **Say:** Minimum: the Must features and nothing else. No menu, no colours, no charts. Viable: a real user could do the job once, start to finish, without you standing next to them. Product: python3 main.py runs on another laptop from a fresh terminal. For the study logger, the MVP is: type one entry, it is saved, the weekly totals print. That is all.
- **Say:** Look at the figure. Everything below the yellow line runs by the end of week 11. Everything above it waits until it does.
- **Ask:** Someone says "I'll add F1 after the menu works." What is wrong?
- **Answer:** The menu is a Could. It is above the line. F1 is the slice; build it first.
- **Next:** Slice is the key word. What is a slice?

## Slide 8 — Slices, Not Layers
- **Time:** 17–20 (3 min)
- **Say:** A slice is one feature through every file. A layer is one file through every feature. F1 for the study logger touches main.py, logic.py and storage.py. Build those three pieces and run it. Every slice ends with a run. A layer ends with nothing to run.
- **Say:** Look at the grid. The green column is F1: main asks and saves, logic makes the record, storage appends it. The red dashed row is storage.py done for all three features: load_records and append_record finished, and still nothing runs.
- **Say:** One more reason. Week 10 asked for one branch per feature. A slice is exactly one branch. Your Git history tells the grader the story for free.
- **Next:** But a slice needs every function it calls. What if some do not exist yet? Fake them.

## Slide 9 — Fake It, Then Make It
- **Time:** 20–23 (3 min)
- **Say:** A fake is a function that returns a constant and ignores its arguments. load_records here returns a hard-coded list. weekly_totals returns a hard-coded dict. Only format_totals is real. Run it and you get "python 90 min". The number is wrong. The shape of the program is right: main calls storage, storage feeds logic, logic feeds report.
- **Say:** The docstring stays true. Only the body is pretending. That matters: when you replace the fake, nothing else changes.
- **Ask:** Why bother with a wrong answer on day one?
- **Answer:** Because now every remaining job is visible as a fake you can point at, and every replacement can be tested against a program that already runs.
- **Next:** In what order do you replace them?

## Slide 10 — Replace One Fake at a Time
- **Time:** 23–25 (2 min)
- **Say:** From the core outward. Logic first, because a logic function needs no file and no keyboard, so one assert proves it in a second. Storage next: one function opens the file, with the header and newline rules done right. Then wire main to the real names and run the whole thing. After every replacement: run the checks, run main, commit.
- **Say:** The figure is four commits. In each row one more box turns green. The program runs in every row.
- **Say:** The rule: never two fakes in one step. When something breaks, you want exactly one suspect.
- **Next:** Sometimes the suspect is a library you have never used. Spike it.

## Slide 11 — Spike in Scratch, Build in the Repo
- **Time:** 25–28 (3 min)
- **Say:** A spike is a throwaway experiment that answers one question. Here the question is: how does csv.DictWriter end a row? Ten lines in a scratch file. The answer: with carriage return and line feed. That is why storage opens the file with newline equals empty string. The answer goes into append_record; the spike goes in the bin.
- **Say:** Spikes break every rule. print everywhere, no docstring, no checks. That is fine, because they are never committed. scratch slash is in your .gitignore from the week 10 starter, so a spike cannot slip into a pull request by accident.
- **Do:** If asked why StringIO: it is a file that lives in memory, so the spike does not even create a file to clean up.
- **Next:** Work, right, fast.

## Slide 12 — Make It Work, Make It Right, Make It Fast
- **Time:** 28–29 (1 min)
- **Say:** Kent Beck's order. First make it work: the slice runs. Then make it right: names, duplication, shape. That is act three. Then make it fast, and we are skipping that one: a twenty-row CSV needs no optimising. Students who try all three at once get none of them.
- **Next:** Your turn, on paper.

## Slide 13 — Practice 1: Draw Your F1 Slice
- **Time:** 29–33 (4 min)
- **Say:** Four minutes. From your design document, list the functions F1 calls, in call order, with their modules. Mark the one you will fake first and write the constant it returns. Then write the proof that F1 works: the acceptance criterion from week 9, as something you can do at the keyboard. This list is your lab plan. Each line becomes one commit.
- **Do:** Circulate. Students whose F1 calls a function that is not in their design document should add it to the document now.
- **Ask:** Which function do you fake first?
- **Answer:** The one whose real body needs a file or the keyboard. Logic can be written for real immediately; storage is the natural fake.
- **Next:** Act two: from stub to body.

## Slide 14 — Structure: Fill the Skeleton
- **Time:** 33–34 (1 min)
- **Say:** Ugly inside a function is allowed this week. Ugly between functions is not. We fill the skeleton one contract at a time, with a check after each, and we keep the week 10 shape while we type: logic raises, main talks, storage opens.
- **Next:** One function, start to finish.

## Slide 15 — From Stub to Body
- **Time:** 34–37 (3 min)
- **Say:** Before: the week 10 stub. The docstring is the contract: a positive whole number of minutes, ValueError otherwise. After: the simplest body that keeps that promise. int converts, one if rejects zero and negatives, return. Then one line proves the good case.
- **Say:** Simple beats clever. If you can think of a shorter body that keeps the contract, use it. You can make it elegant in act three.
- **Ask:** What happens with "abc"?
- **Answer:** int raises ValueError on its own. The contract is kept without an extra line.
- **Next:** Storage.

## Slide 16 — Storage: One Function Opens the File
- **Time:** 37–40 (3 min)
- **Say:** append_record is the only code in the project that knows the file format. Everyone else sees dicts. Three details, all from the design and the spike. newline equals empty string, because csv writes its own line endings. Mode a appends. The header is written once, only if the file did not exist. FIELDS is the one place the column order lives.
- **Say:** Run it and print the file: the two sample rows from week 10, and the new one.
- **Ask:** Why does FIELDS live in storage.py and not in logic.py?
- **Answer:** Column order is a fact about the file. Only storage talks to the file. logic deals in dicts, where order does not matter.
- **Next:** Now main.

## Slide 17 — Wire main() for F1 Only
- **Time:** 40–43 (3 min)
- **Say:** main asks three questions, tries make_record, and either prints the ValueError as a sentence or appends the record and says Saved. Nothing about F2 or F3. The slice is F1, so main is F1. Run it from the project folder, type an entry, then open data/study.csv and look at the new row.
- **Do:** Run it live in examples/study_logger_f1. Then run it again with -30 and show that the file did not change.
- **Next:** A trap that prototyping invites.

## Slide 18 — TRAP: The Shortcut That Leaks
- **Time:** 43–46 (3 min)
- **Say:** "It is just a prototype, so I printed the error and returned None." Two minutes later, the caller does what the contract promised it could do: it reads the course from the dict. It got None. TypeError. Here the crash is one line below. In your project it is three files away, and the message does not mention minutes at all.
- **Say:** The rule for this week: prototype inside the body all you like. The boundary keeps its promise. A dict, or a raise. Never a print and a None.
- **Ask:** Fix it in one word.
- **Answer:** Replace print with raise. The caller's except already exists.
- **Next:** The rhythm of the lab.

## Slide 19 — Run, Then Commit
- **Time:** 46–49 (3 min)
- **Say:** One step, one run, one commit. test_logic.py proves the core; main.py proves the slice; both before every commit. The message names the function, so the log reads like your design document being ticked off: skeleton, main with fakes, parse_minutes, make_record, append_record.
- **Say:** These five hashes are real. The script in instructor slash slice_demo.sh replays them. Small commits are free undo points. One big commit is a bet you cannot take back.
- **Next:** Where do the checks come from?

## Slide 20 — Grow test_logic.py with Every Function
- **Time:** 49–51 (2 min)
- **Say:** Every logic function gets one check before you move on. The good case as an assert. The bad cases in a loop that must raise ValueError, with an AssertionError if one slips through. Only logic is tested here, so it finishes in a second, and you run it before every commit.
- **Say:** Notice the sentences. Week 9: "entering -30 prints a warning and saves nothing." Week 10: "raises ValueError if minutes is not positive." Week 11: make_record with -30 must raise. The same sentence, three times.
- **Next:** When is F1 done?

## Slide 21 — Done Means Running
- **Time:** 51–52 (1 min)
- **Say:** A slice is done when every line here is true. Checks pass. main saves a valid entry. A bad entry is refused and the file is unchanged. No I/O in logic. Every step is a commit on the feature branch. The branch is pushed and the pull request is open. "Almost done" is a fake: either the row is in the file or it is not.
- **Next:** Break.

## Slide 22 — Halftime
- **Time:** 52–62 (10 min)
- **Say:** Ten minutes. When we return: the same program, a better shape. Then the lab.
- **Do:** Help anyone whose repository check from slide 4 still fails. They need a clean, running skeleton before the lab.

## Slide 23 — Refactor: Same Behavior, Better Shape
- **Time:** 62–63 (1 min)
- **Say:** Act three. Refactoring means changing how the code is written without changing what it does. Five small moves, each one commit. Checks green before, checks green after. If you cannot say that, it was not refactoring; it was rewriting.
- **Next:** Two hats.

## Slide 24 — Two Hats
- **Time:** 63–65 (2 min)
- **Say:** Adding behaviour and improving shape are different jobs. Feature hat: make a check pass that failed; the output changes on purpose. Refactor hat: output identical, structure better; the checks prove it stayed identical. You switch hats only at a commit. Never "while I'm in here".
- **Say:** In this course: feature hat during the lab, refactor hat before every pull request.
- **Next:** The five moves.

## Slide 25 — Five Smells, Five Moves
- **Time:** 65–67 (2 min)
- **Say:** You do not need a textbook. A name that says nothing: rename. The same three lines twice: extract a function. A bare number or string that means something: name a constant. An if inside an if inside an if: guard clauses. A function taller than your screen: split it by the verb test from week 10.
- **Say:** Each move is one commit, and the checks run before and after each one.
- **Next:** Let us do three of them on real code.

## Slide 26 — Before: It Works. Now Read It Aloud
- **Time:** 67–69 (2 min)
- **Say:** Every check passes on this function. Now say what it does in one sentence. What is t? What is k? What does show show? Two branches, two f-strings: read them side by side.
- **Ask:** Are the two branches really different? Compute 45 // 60 and 45 % 60.
- **Answer:** 0 and 45. So the else branch produces exactly what the if branch would. The branches are identical; the duplication hid it.
- **Say:** That is a smell. Not a bug: the output is correct. A cost: every reader pays it.
- **Next:** After three moves.

## Slide 27 — After: Same Output, Half the Reading
- **Time:** 69–71 (2 min)
- **Say:** Rename: totals, course, minutes, the names from the design document. Extract: format_duration has one job and one home. Delete the branch that was never different. Same two output lines. One commit: Refactor: extract format_duration.
- **Do:** Point at the two OUTPUT boxes on slides 26 and 27. Identical, character for character. That is the test.
- **Next:** Guard clauses.

## Slide 28 — Guard Clauses: Fail Early, Then Relax
- **Time:** 71–72 (1 min)
- **Say:** Before: nested ifs. To read the last line you hold two conditions in your head. After: handle the bad cases at the top and leave. The happy path reads straight down and the normal answer is the last line, unindented, where the eye expects it.
- **Next:** Duplication.

## Slide 29 — Duplication: Write It Once, Call It Twice
- **Time:** 72–73 (1 min)
- **Say:** Two functions that differ in one word. That word becomes a parameter. Fix a bug in one place and both callers get it. Rule of three: the second copy is a warning, the third is a job.
- **Next:** The trap of this act.

## Slide 30 — TRAP: Refactoring Blind
- **Time:** 73–74 (1 min)
- **Say:** Refactoring without a check is rewriting with your eyes closed: you cannot know the output stayed the same. And a mixed commit, "Implement F2 and rename stuff and fix bug", hides four decisions; when it breaks, every line is a suspect. Refactor on the branch, after the slice runs, one move per commit, message starting with Refactor colon. That prefix is a promise: the checks passed before and after.
- **Next:** Practice.

## Slide 31 — Practice 2: Tidy Without Breaking
- **Time:** 74–82 (8 min)
- **Say:** Eight minutes. Open labs slash session2 slash tidy_lab.py and run it: six PASS. Apply three moves, one at a time: rename the variables, name the constant 2000, extract the duplicated line. Run after every move. Still six PASS? Next move. A FAIL? Undo the last move.
- **Do:** Solution: instructor/solutions/tidy_lab.py. Common error: renaming a function that the checks call. The check calls stay; rename variables and parameters.
- **Ask:** Early finishers: what does the else-if in goal_status do?
- **Answer:** Nothing the first if did not already decide. A guard clause removes it: return "under" after the if.
- **Next:** The lab.

## Slide 32 — Lab: Ship Your F1
- **Time:** 82–83 (1 min)
- **Say:** Thirty minutes. Your project, your branch, from stub to merged pull request. Three steps: branch and fake, replace the fakes, tidy and ship. The sheet is labs slash session2 slash slice-lab.md. The finished study logger is in examples slash study_logger_f1 if you want to compare.
- **Next:** First, the errors you will meet.

## Slide 33 — When It Does Not Run
- **Time:** 83–84 (1 min)
- **Say:** Read the last line of the traceback first. It names the problem. The line above it names your file and line. These five cover most of what you will see today. No module named logic: wrong folder. NotImplementedError: a stub is still on the path, and it is simply your next function. Concatenate str: a value is still text. FileNotFoundError: the data folder is missing. Nothing printed: the main guard is missing.
- **Do:** Leave this slide on the projector during the lab; flip to the step slides as the clock moves.
- **Next:** Step one.

## Slide 34 — Lab Step 1: Branch and Fake
- **Time:** 84–90 (6 min)
- **Say:** Six minutes. Switch to main, pull, create your feature branch. In main.py write main for F1 only: ask for its inputs, call its functions by their design names, print the result. Every function you call must exist; give the unwritten ones a fake body that returns a constant of the right shape. Run main. No traceback allowed. Commit.
- **Do:** Circulate. The common block: a NotImplementedError from a stub main calls. That stub needs a fake body, not a real one, for now.
- **Next:** Step two.

## Slide 35 — Lab Step 2: Replace the Fakes
- **Time:** 90–104 (14 min)
- **Say:** Fourteen minutes. One function at a time, core first. Read the contract, write the body. For a logic function, add one check to test_logic.py. Run test_logic.py, run main.py, commit with the function's name. Then the next fake. Stuck for more than three minutes on a library? Spike it in scratch and come back.
- **Say:** Do not touch F2 or F3. If a function is shared, implement only what F1 needs today.
- **Do:** Watch for input or print creeping into logic functions. Ask: who calls this, and can a test see that print?
- **Next:** Step three.

## Slide 36 — Lab Step 3: Tidy, Push, Pull Request
- **Time:** 104–112 (8 min)
- **Say:** Eight minutes. Refactor hat on: design names, one constant for the file path, no dead branches. Run the checks, commit as Refactor colon. Push the branch, open the pull request with the four headings, self-review the Files changed tab, merge, delete the branch, switch to main and pull.
- **Say:** Not finished? Push what you have and submit the open pull request. Finish before next session. The slice must run before F2 starts.
- **Next:** What usually goes wrong this week.

## Slide 37 — Five Ways to Lose Week 11
- **Time:** 112–114 (2 min)
- **Say:** Building layers. Prototyping across the boundary. Refactoring without checks, or mixing it with a feature. Gold-plating: a menu, colours, a chart, before F1 saves a single row. And one commit on Friday called "mvp", which proves nothing to the grader.
- **Next:** Quick check.

## Slide 38 — Exit Check
- **Time:** 114–118 (4 min)
- **Say:** One line each, then compare with a neighbour.
- **Answer:** 1. One feature through every file; it runs after each session and gives every bug one place to be. 2. A constant of the right shape; the docstring and the call sites stay real. 3. python3 test_logic.py and python3 main.py. 4. Behaviour unchanged, shape improved; identical output from the checks before and after. 5. Rename for meaningless names, extract for duplication, constant for magic values, guard clause for nesting, split for long functions.
- **Next:** Submission.

## Slide 39 — Submit and Next Session
- **Time:** 118–120 (2 min)
- **Say:** Submit the merged pull request link and your git log today. If the branch is not merged, push it and submit the open pull request, then finish before next session. Next session: F2 and F3 as slices, then a refactor pass across all four files, and at the end the MVP demo: python3 main.py does every Must feature, start to finish.
- **Say:** One branch and one pull request per Must feature. Every commit is yours.
