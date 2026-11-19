# Week 5 — Three moves: sequence, condition, repetition

Computational Thinking

A first-year vocational ICT course

---

## The central message

**Almost any process can be described with three building blocks: sequence, condition, and repetition.**

Once you can name them in everyday tasks, you have the skeleton of every program.

---

## What this week trains

- Lesson 13 — **sequence**: doing things in order
- Lesson 14 — **conditions**: deciding what to do next
- Lesson 15 — **repetition**: doing the same thing again, with a stop

Plain English only. No code yet.

---

## Sequence — the default move

A sequence is doing one step after another, in a fixed order.

A tea recipe:

1. Fill the kettle.
2. Switch it on.
3. Put the tea bag in the mug.
4. Pour boiling water.

---

## When order matters

Swap step 2 and step 4:

1. Fill the kettle.
2. *Pour boiling water.*
3. Put the tea bag in the mug.
4. *Switch the kettle on.*

A literal follower pours cold water and watches an empty kettle. The order you write is the order you get.

---

## Sequence at work — deployment checklist

1. Merge the new branch.
2. Run the build.
3. Run the smoke tests.
4. Deploy to staging.
5. Get sign-off.
6. Deploy to production.

Same shape as the tea recipe. Several steps cannot be reordered without breaking the process.

---

## Condition — a test that splits the path

A condition is a test that decides which step happens next.

*"If it rains, take the bus, else walk."*

The condition is the moment the path forks.

---

## if … then … else …

Everyday: *if it rains, then take the bus, else walk.*

IT mirror: *if the password is shorter than 8 characters, then reject it, else accept it.*

Same shape. Different scene.

---

## Decision tree — drawing the split

```
        Is it raining?
        /            \
      yes             no
      /                \
take the bus         walk
```

Pen and paper is enough. The drawing forces an honest test at every branch.

---

## Condition at work — password validation

- **if** shorter than 8 chars, **then** reject
- **if** no number, **then** reject
- **if** no capital letter, **then** reject
- **otherwise** accept

A chain of conditions ending in two outcomes.

---

## Repetition — doing it again, with a stop

A repetition is doing the same step more than once, with a stopping condition the follower can see.

Everyday: *for each name in the register, mark present or absent.*

---

## Three shapes of repetition

- **for each** — the list is known in advance.
- **repeat until** — the stop depends on what happens.
- **while** — the test is checked before each repeat.

All three need an honest, observable stop.

---

## Repetition at work — the inbox sweep

> **for each** unread message in the inbox:
> &nbsp;&nbsp;&nbsp;&nbsp;**if** from a person, mark for reply;
> &nbsp;&nbsp;&nbsp;&nbsp;**else if** newsletter, archive;
> &nbsp;&nbsp;&nbsp;&nbsp;**else if** spam, delete.
> Repeat until the inbox is empty.

All three building blocks in one process.

---

## The stopping condition is the safety belt

Honest stop: *"until the inbox is empty"*, *"until the timer hits 30 seconds"*.

Not a stop: *"until you feel done"*, *"until you understand"*.

A runaway repetition has no honest stop. The fix is a safety stop in plain English.

---

## Three moves in one process

Most real processes are a weave:

- a small **sequence** inside
- a **condition** that chooses what to do
- a **repetition** that does it for every item

Naming the three is what makes the description readable.

---

## Must-do minimum vs. deepening

**Must-do minimum**
- Name the three building blocks in an everyday process.
- Combine all three into one short process description.

**Deepening**
- Compound conditions (AND, OR).
- Safety stops on runaway repetitions.
- Vocational scenes: password rule, ticket routing, inbox sweep.
- LLM sparring with a structured prompt.

---

## Tasks this week

- Task 5.1 — Three moves in one process (MANDATORY, AT2 feeder)
- Task 5.3 — Decision tree for a real rule (DEEPENING)
- Task 5.4 — The stopping condition is the safety belt (DEEPENING)
- Task 5.5 — Vocational angle, optional LLM sparring (DEEPENING)

Keep your notes — AT2 lands at the end of Week 5 / during Week 6.

---

## What comes next: Week 6 — pseudocode

The natural-language descriptions you write this week get a few small conventions added: simple variables, light indentation, a trace table.

The thinking stays the same. The shape just tightens.

---

## Recap — the central message, one more time

**Almost any process can be described with three building blocks: sequence, condition, and repetition.**

Once you can name them in everyday tasks, you have the skeleton of every program.
