# Vocabulary

## Week 2 vocabulary

The terms below cover Lessons 4, 5 and 6. Definitions are short on purpose — the self-study has the examples in context. One term at the end (*abstraction*) is a preview of Week 3, flagged as such. *Decomposition* was previewed in Week 1; this week it gets its full definition.

### Decomposition
The move of taking a task that is too big for one flat list of steps and splitting it into a **main task** with a **goal** and a small set of **subtasks**, each with its own sub-goal. Decomposition is a planning move — the actual steps still have to exist underneath, just at a manageable size. *"Make breakfast for four people"* decomposes into *decide the menu*, *check the fridge*, *prepare hot food*, *prepare cold food*, *set the table*, *call everyone to the table*.

### Main task
The top-level task you are trying to carry out. The main task has one **goal** — a short sentence that says what the end state should look like. *"Make breakfast for four people by 8:30"* is a main task; its goal is *"everyone is eating breakfast by 8:30."*

### Subtask
A smaller task that lives under the main task. A subtask is small enough that you can write a clean little algorithm for it (one short sequence of literal steps), and it has its own **sub-goal**. *"Prepare hot food"* is a subtask of *"make breakfast for four people"*.

### Sub-goal
The goal of one specific subtask, written in a single sentence. A sub-goal is not the same as the main task's goal — it is narrower and more specific. The sub-goal of *"prepare hot food"* might be *"scrambled eggs and toast are warm and on a serving plate."*

### Goal (revisit)
What a task is trying to achieve — the end state. You met *goal* in Week 1 for an algorithm; this week it applies both to the main task and, separately, to every subtask. A good rule of thumb: if you cannot write the goal in one short sentence, the task is still too big or too vague.

### Dependency
A connection between two subtasks where one needs the **output** of another before it can start. *"Pour the water into the cup"* depends on *"boil the water"*, because the boiling subtask's output (hot water) is the pouring subtask's input. Dependencies pin some subtasks into a fixed order; subtasks without a dependency on each other have a free order.

### Order (of subtasks)
The sequence in which subtasks are actually carried out. Order is not free — dependencies constrain it. Two subtasks with no dependency on each other can come in any order, but a sensible default order still helps a literal follower.

### Sequence (revisit)
A list of things in order. In Week 1 you wrote algorithms as a sequence of steps; in Week 2 you write a sequence of **subtasks**, where each subtask is itself a small sequence of steps.

### Prerequisite
A condition that must be true before you can start a subtask. A prerequisite is close to a dependency but not identical: a dependency is a connection between two subtasks, while a prerequisite is a state of the world ("the laptop is unboxed and switched on") that has to hold before the subtask can begin. Many prerequisites are satisfied by another subtask's output, which is when the two ideas overlap.

### Parallel (informal sense only)
Two subtasks are *parallel* when they have no dependency on each other and could happen at the same time — for example, two people doing them at once, or one person switching between them. In this course *parallel* is used in the everyday sense only; the technical idea of concurrency is **not** introduced this week.

### Parent task
Another name for the main task when you want to stress the hierarchy: the parent task sits above its subtasks. *"Onboard a new colleague"* is the parent task of *"order a laptop", "set up email", "introduce to the team."*

### Hierarchy
The informal shape of a decomposition: one main task at the top, subtasks underneath. If a subtask is itself big enough, you can decompose *it* into smaller subtasks, and the hierarchy goes one level deeper. Week 2 stays at one or at most two levels deep.

### Literal follower (revisit)
The Week 1 idea, still in force: every subtask, on its own, must be writeable as a clear sequence of literal steps a literal follower could carry out. Decomposition does not retire the literal-follower mindset; it stacks on top of it.

### AT1
The first assessed task of the course. It is submitted at the end of Lesson 6. AT1 asks you to decompose one task (everyday or IT-related) into a main task with a goal, 4–8 subtasks with sub-goals, and an order with at least one dependency called out. The notes you keep from this week's tasks become your raw material.

### Abstraction *(looking ahead — central topic of Week 3)*
The move of hiding the detail you do not need and keeping only what matters. Week 3 introduces it formally; for now, notice that when you say *"prepare hot food"* as a subtask you are already abstracting — you are not yet saying *which* hot food, on *which* pan, at *which* temperature. That hiding is what makes the subtask name useful at the planning level.
