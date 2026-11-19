# Week 3 — Drawing the process

Computational Thinking

A first-year vocational ICT course

---

## Where Week 2 left off

- You can decompose a problem into a main task, subtasks and sub-goals
- AT1 was submitted at the start of this week
- This week asks: how do I write the process down so someone else can run it?

---

## The Week 3 central message

> *"Once you can decompose a problem, the next skill is to describe the process so someone else can run it — and to decide which details matter and which can be safely hidden."*

---

## What this week trains

- Lesson 7 — the simple flowchart, the first picture in the course
- Lesson 8 — abstraction: choosing what to leave out
- Lesson 9 — reusable instructions: the idea of a function without code

---

## When a list is not enough

A morning routine works as a flat list — alarm, wash, dress, eat, leave.

The moment a yes/no question appears (*"is it raining?"*), the list breaks.

A flowchart is what a list becomes when a process has a branch.

---

## The four shapes

- **Oval** — start / end
- **Rectangle** — one step (an action)
- **Diamond** — one yes/no decision, two outgoing arrows
- **Arrow** — the flow from one shape to the next

Four shapes. That is the whole vocabulary of the picture.

---

## A flowchart for "should I bring an umbrella?"

```
( Start ) -> [ Check the weather forecast ]
   -> < Is rain probability > 50% ? >
        Yes -> [ Bring umbrella ]
        No  -> [ Leave umbrella at door ]
   -> ( Leave the house )
```

Eight shapes. One Start, one End, three rectangles, one diamond, arrows everywhere.

---

## IT example — help-desk triage

- *Read the ticket*
- *Can the user log in now?*
  - Yes → close the ticket
  - No → ask the user for a screenshot

One diamond, two paths, two different End ovals.

---

## Abstraction — hide the detail that does not matter

Abstraction is **choosing what to leave out so the description fits the audience**.

Not vagueness — the boxes you do draw stay precise.

Not philosophy — a bus stop, a Login button, a file name.

---

## A bus stop is an abstraction

- **Passenger** — a sign saying "Park Street" and a timetable
- **Dispatcher** — a GPS coordinate, an ID number, a list of buses
- **Engineer** — a junction box, a power cable, screws

Same physical thing. Three abstractions. Three right answers.

---

## The "Login" button is an abstraction

Hidden inside it:

- the identity server
- the password check (against an encrypted store)
- the session cookie
- the OAuth dance (if sign-in goes through Microsoft or Google)

The button is the right description *for the user*.

---

## Level of detail follows the audience

- **New help-desk hire, day one** — six rectangles before the diamond
- **Senior IT admin, ten years in** — one rectangle before the diamond

Same process. Same goal. Different audience. Different level of detail.

Both flowcharts are correct.

---

## Reusable instructions — give the chunk a name

Two flowcharts. Both contain *Open the portal → enter username → enter password → press Login → wait for landing page*.

Five rectangles, twice.

Or: one named block — *"log the user in"*.

---

## A function (Week 3 sense)

- **Named** — a short verb-phrase
- **Reusable** — appears in many processes
- **Plain English description** — one short paragraph
- **Input** — what it needs to start
- **Output** — what it produces when done

Not code yet. Just a labelled box and a paragraph.

---

## Vocational example — "register a new device"

Used every time a new laptop, projector or conference-room display arrives.

A ten-box flowchart for *"set up a new conference room"* becomes a seven-box flowchart when *"register a new device"* is one named box.

The five hidden steps still exist — filed in the school's IT handbook.

---

## Week 3 vocabulary at a glance

- *process, flowchart, start/end, step, decision, arrow, branch, Yes/No path*
- *abstraction, level of detail, hidden detail, audience*
- *reusable block, named block / function (Week 3 sense)*
- *trade-off; condition* (looking ahead — Week 5)

---

## Must-do minimum vs. deepening

**Must-do minimum**
- Define the core terms
- Read a small flowchart and describe what it does
- Draw a small flowchart from your own life with a decision
- Name two hidden details inside one abstraction
- Spot one reused chunk and name it

**Deepening**
- Rewrite one step at a lower level of detail
- Find three reusable blocks across two processes
- LLM sparring partner on abstraction choices

---

## Tasks this week

- Task 3.1 — Draw your first flowchart (MANDATORY)
- Task 3.3 — What's hidden inside the Login button? (DEEPENING)
- Task 3.4 — Spot the reused chunk (DEEPENING)
- Task 3.5 — Rewrite a step at a lower level of detail (DEEPENING)

Keep your notes — they feed into AT2 at the end of Week 5 / during Week 6.

---

## What comes next: Week 4 — alternative solutions

More than one valid flowchart can reach the same goal.

Week 4 asks: how do you compare two valid solutions and choose?

Same flowchart skill; new question on top.

---

## Recap — the central message, one more time

> *"Once you can decompose a problem, the next skill is to describe the process so someone else can run it — and to decide which details matter and which can be safely hidden."*
