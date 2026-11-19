# Vocabulary

## Week 5 vocabulary

The terms below cover Lessons 13, 14 and 15. Definitions are short on purpose — read the self-study for examples in context. One term at the end (*pseudocode*) is a preview of Week 6, flagged as such.

### Sequence
Doing one step after another, in a fixed order, unless the instruction tells you otherwise. Sequence is the default move in any process: when no condition and no repetition is written, a literal follower walks the steps top to bottom. A recipe and a deployment checklist are both sequences.

### Step
One single action in a process. A good step is small enough that a literal follower can carry it out without asking a clarifying question. "Switch the kettle on" is a step; "make breakfast" is a whole process. (Revisited from Week 1, used the same way here.)

### Order
The position of each step in a sequence — which step comes first, second, third, and so on. The order matters when later steps depend on the result of earlier ones; pouring boiling water before putting the tea bag in is not the same drink as the other way around.

### Dependency
The light, intuitive idea that one step needs the result of an earlier step before it can run. Boiling the water is a dependency of pouring it. Two steps with no dependency between them can sometimes be swapped without breaking the process; two steps with a dependency cannot.

### Condition
A test that decides which step happens next. A condition is the moment in a process where the path splits in two (or more). "If it rains, take the bus, else walk" is a condition with two branches; "if the milk smells off, throw it out" is a condition with one branch and no alternative.

### Test (as part of a condition)
The question a condition asks the follower. *"Is the password shorter than 8 characters?"* and *"Is it raining now?"* are tests. A good test is something a literal follower can actually check; a bad test (*"will I be late?"*, *"is it going wrong?"*) leaves the follower guessing. (Revisited from Week 1 with a new meaning here.)

### Branch
One of the paths leading out of a condition. A two-branch condition has a *then*-branch and an *else*-branch; a three-branch condition adds an `else if`. Each branch ends in either a step (a leaf) or another condition (a deeper split).

### Decision tree
A picture of a condition (or a chain of conditions). The root is the first test; each branch is a possible answer; each leaf is either a final step or another test. Drawing a decision tree on paper is the fastest way to see whether a rule has the right number of branches.

### If-then
The shorter shape of a condition: *if X is true, then do A.* There is no alternative — if X is false, the follower does nothing extra and moves on. *"If you finish your homework before dinner, you can play games"* is an if-then.

### If-then-else
The longer shape of a condition: *if X is true, then do A; else do B.* The follower always does one of the two; the *else* names the alternative. *"If it rains, take the bus, else walk"* is an if-then-else.

### Repetition
Doing the same step or block of steps more than once, with a stopping condition that tells the follower when to stop. Repetition is also called a *loop* in everyday tech speak — both words mean the same thing in this course. "Mark each name in the register" and "keep stirring until the sugar dissolves" are both repetitions.

### For-each
The shape of a repetition where the list of items is known in advance. *"For each name in the register, mark present or absent."* The follower does the inside step once for every item in the list, and stops when the list is finished.

### Repeat-until
The shape of a repetition where the stop depends on what happens. *"Keep stirring until the sugar dissolves."* The follower does the inside step, checks the stopping condition, and either stops or repeats.

### While
The shape of a repetition where a continuing condition is checked *before* each repeat. *"While the kettle is still hot, do not boil it again."* As soon as the condition stops being true, the follower stops repeating.

### Stopping condition
The honest, observable test that ends a repetition. "Until the inbox is empty" is a stopping condition; "until I feel done" is not, because nobody else can check it. Every repetition needs a stopping condition the follower can actually see.

### Runaway repetition
A repetition whose stopping condition can never become true, so the follower would keep going forever. *"Repeat until you understand"* is a runaway repetition unless "understand" is replaced by something observable (e.g. "until you can explain it back to a classmate in one sentence"). The safety belt against runaway repetitions is an honest stopping condition.

### Pseudocode *(looking ahead — central topic of Week 6)*
A tighter, more rule-bound way of writing process descriptions on paper — closer to code, but still not code. Week 5 stays in loose natural language. Week 6 adds a few small conventions (indentation, simple variables, a trace table) that turn the descriptions you write this week into pseudocode. You do not need to know pseudocode yet.
