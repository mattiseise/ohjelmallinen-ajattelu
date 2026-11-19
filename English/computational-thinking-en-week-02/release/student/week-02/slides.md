# Week 2 — Decomposing problems

Computational Thinking

A first-year vocational ICT course

---

## What we covered in Week 1

- A computer follows instructions literally
- An algorithm is a clear sequence of literal steps
- Ambiguity is in the instruction, not in the follower

---

## This week's central message

> *"A big problem becomes a manageable problem once you name the main task, its subtasks, and the order in which they have to happen."*

---

## What is decomposition?

The move of taking a task that is too big for one flat list of steps and splitting it into a **main task** with a **goal** and a small set of **subtasks**, each with its own sub-goal.

A planning move. The steps still exist underneath — just at a manageable size.

---

## Main task, subtasks, goal

- **Main task** — what you are doing, in one sentence
- **Goal** — what is true at the end, in one sentence
- **Subtask** — a smaller task under the main task
- **Sub-goal** — the goal of one subtask, narrower than the main goal

---

## Everyday example — making breakfast for four

- **Main task:** make breakfast for four by 9:30
- *Decide the menu*
- *Check the fridge*
- *Prepare hot food*
- *Prepare cold items*
- *Prepare the drinks*
- *Set the table*
- *Call everyone to the table*

---

## IT example — creating a user account

- **Main task:** create a new student's account on the school platform
- *Collect the student's details*
- *Choose a username*
- *Create the account in the admin tool*
- *Send the confirmation*

Four small subtasks, each with its own sub-goal.

---

## Why decompose at all?

- You can write each subtask as a clean small algorithm
- You can give different subtasks to different people
- You can check your work subtask by subtask — checkpoints

---

## Some subtasks depend on others

A **dependency** is a connection where one subtask needs the **output** of another before it can start.

*"Eat the toast"* depends on *"toast the bread"*.

Without the toaster's output, the eating subtask has no input.

---

## Some subtasks are independent

*"Set the table"* does not depend on *"prepare the hot food"*. Either order works.

In this course, we call these **parallel** in the everyday sense — "could happen at the same time".

Concurrency is not introduced this week.

---

## Putting subtasks in order — birthday party

**Out of order:** buy the cake, pick the date, music, guest list, send invitations, tidy, snacks, decorate.

**Defensible order:** pick the date → guest list → send invitations → (cake, snacks, tidy, decorate, music fill in where they fit).

Some subtasks are pinned by dependencies. Others are free.

---

## IT example — sharing a file

- *Find the document*
- *Identify the class group*
- *Set the sharing permissions*
- *Copy the share link* — depends on permissions
- *Write the email body* — free of the link
- *Send the email* — depends on link and body

---

## Decomposing a real IT task — Lesson 6 preview

> *"Set up a new colleague's email account on their new laptop in time for their 10:00 start."*

Main task, goal, 6 subtasks, 4 dependencies, one free branch (preparing the laptop runs in parallel with creating the account).

---

## Two valid decompositions of one task

Another colleague might decompose the same task differently — merging two subtasks because their tool does both in one click, or splitting one because at their school it is two different people's jobs.

Both can be valid. Week 4 returns to "how to compare two valid solutions".

---

## Week 2 vocabulary at a glance

- *decomposition*, *main task*, *subtask*, *sub-goal*
- *goal* (revisited), *sequence* (revisited)
- *dependency*, *order*, *prerequisite*, *parallel*
- *parent task*, *hierarchy*
- *AT1*; *abstraction* (looking ahead — Week 3)

---

## Tasks this week

- Task 2.1 — Decompose one task from your own week (MANDATORY)
- Task 2.2 — Decompose with a partner, then re-test (MANDATORY)
- Task 2.3 — Order and dependencies (DEEPENING)
- Task 2.4 — Vocational angle: decompose an IT task at your school (DEEPENING)
- Task 2.5 — Sparring partner: challenge your own decomposition (DEEPENING)

---

## AT1 — the first assessed task

Submitted at the **end of Lesson 6**.

Bring an artefact that has:

- A main task and its goal
- 4–8 subtasks with sub-goals
- An order with at least one dependency called out
- A 3–5 sentence reflection

Your notes from this week are the raw material.

---

## What comes next: Week 3 — abstraction and flowcharts

Week 3 adds **abstraction** — hiding the detail you do not need.

It also introduces the first picture of a process: a simple flowchart (start, end, arrows). No code yet.

---

## Recap — the central message, one more time

> *"A big problem becomes a manageable problem once you name the main task, its subtasks, and the order in which they have to happen."*
