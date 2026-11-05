# User Scenarios — {Project Topic}

| Item | Details |
|---|---|
| Team name | |
| Team members (name / student ID) | |
| Submission date | |
| Document version | v1 |

> Instructions: Fill in the placeholders marked with `{ }`, then delete the guidance lines (lines starting with >).
> Reference scenario IDs (SC-01, SC-02, etc.) in the "Related scenarios" column of the specification workbook's Requirement sheet.
> Minimum: At least two scenarios (including one exception case), a system architecture description, and a division of responsibilities.

## 1. Project Overview

> Describe the problem this program addresses and its core idea in 3–5 sentences.

{Overview}

## 2. Users

> Identify who uses this program (e.g., a server administrator, developer, or another process).

| User | Description |
|---|---|
| {User 1} | {Role and purpose} |

## 3. Scenarios

### SC-01. {Scenario Title}

- **User**: {Who}
- **Context**: {When and under what circumstances}
- **Goal**: {What the user wants to accomplish in this scenario}

**Workflow**

1. {User action}
2. {Program response}
3. {…}

**Example Execution**

```bash
$ ./program {options} {arguments}
{Expected output}
```

**Outcome**: {State when the scenario ends}

### SC-02. {Exception Scenario Title}

> Include at least one exception scenario, such as invalid input, concurrent execution, or termination during execution (Ctrl+C, kill).

- **User**: {Who}
- **Context**: {What exception occurs}
- **Expected behavior**: {How the program should respond}

**Workflow**

1. {…}
2. {…}

**Example Execution**

```bash
$ ./program {options} {arguments}
{Expected output}
```

**Outcome**: {Resource cleanup, data state, etc.}

## 4. System Architecture

### 4.1 Processes and Threads

> Describe the processes (or threads) and what each does. A text diagram is sufficient.

```text
{Example}
[main] ──fork──▶ [worker 1]
   │   ──fork──▶ [worker 2]
   └── Reap child processes with waitpid; on SIGINT, terminate children and clean up.
```

| Process / Thread | Role | Creation / Termination |
|---|---|---|
| {Name} | {Role} | {fork/exec, pthread_create, waitpid, etc.} |

### 4.2 IPC and Synchronization

> Describe how processes exchange data or prevent concurrent access (pipes, FIFOs, message queues, shared memory, semaphores, file locks, signals, etc.). Write "None" if not applicable.

| Where Used | Method | Reason |
|---|---|---|
| {Where} | {What} | {Why} |

### 4.3 Data Storage Format

> Describe the formats of files, records, and messages that the program reads and writes.

| File / Data | Format (Text / Binary) | Structure |
|---|---|---|
| {Filename} | {Format} | {Fields, e.g., `struct record { uint32_t id; char name[32]; uint32_t crc; }`} |

## 5. Division of Responsibilities

| Team Member | Responsibility |
|---|---|
| {Name} | {Assigned feature IDs or tasks} |

## 6. Additional Notes

{Complete if needed}
