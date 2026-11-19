# Vocabulary

## Week 3 vocabulary

The terms below cover Lessons 7, 8 and 9. Definitions are short on purpose — the self-study has each term in context with examples. One term at the end (*condition*) is a preview of Week 5, flagged as such. *Abstraction* was previewed in Week 2; this week it gets its full definition.

### Process

A sequence of steps that takes you from a starting point to an ending point, sometimes with a decision along the way. A morning routine is a process. A help-desk ticket from "opened" to "closed" is a process. In Week 1 you wrote processes as flat lists; in Week 3 you draw them as flowcharts when the list has branches.

### Flowchart

A picture of a process built from four basic shapes — start/end (oval), step (rectangle), decision (diamond), and arrows. A flowchart is what a list becomes when the process has a branch the list cannot show. It fits on a page when each box stays at the right level of detail.

### Start / end (oval)

The oval that opens or closes a flowchart. Every flowchart has exactly one **Start** oval and at least one **End** oval. The Start says where the process begins; an End says where one path stops. If your flowchart has two ways to finish (for example *"ticket closed"* and *"ticket escalated"*), you draw two End ovals.

### Step (rectangle)

A rectangle that holds one action in the process — *"Check the weather forecast"*, *"Save the file"*, *"Send the ticket to the user"*. A step is a single thing the follower does. If a step turns out to be three things, you either break it into three rectangles or hide them inside a named block.

### Decision (diamond)

A diamond that holds one yes/no question — *"Is rain probability above 50%?"*, *"Does the file name match the convention?"*, *"Can the user log in?"*. A decision diamond has two outgoing arrows, one for each answer. The diamond is the shape that a flat list cannot draw; it is the reason flowcharts exist.

### Arrow / flow

An arrow shows the order in which the follower moves through the flowchart. Arrows go from one shape to the next. Every shape has at least one outgoing arrow (except End ovals); decision diamonds have exactly two.

### Branch

A point in the flowchart where the process splits into more than one path because of a decision. The two arrows coming out of a decision diamond are the two branches. A flowchart with no branches is just a list with boxes drawn around it.

### Yes/No path

The label on each of the two arrows coming out of a decision diamond. Use *Yes / No* when the question is a yes/no question. Use *Match / No match*, *Pass / Fail* or similar when those words read more clearly than yes/no — the rule is *each branch has its own short label*.

### Abstraction

The move of **hiding the detail that does not matter at the level you are describing**. Abstraction is not vagueness; the boxes you do draw are still precise. It means choosing what to leave out so the description fits the audience. A bus stop on a city map is an abstraction. A "Save" button is an abstraction. Abstraction is the Week 3 idea that decides which boxes deserve to be drawn and which can stay hidden.

### Level of detail

How zoomed-in the boxes in a flowchart are. *"Check the file name"* is one level of detail. *"Open the file → look at the date prefix → look at the topic part → compare against the convention"* is a lower (more zoomed-in) level of detail of the same step. A flowchart works when all its boxes are at roughly the same level of detail, chosen for the same audience.

### Hidden detail

A detail that is **deliberately not shown** at this level of detail, but is still known and findable elsewhere. Hidden ≠ forgotten. When the "Login" button hides the password store and the cookie, those details still exist; they just do not belong on the button.

### Audience (of a description)

The person who will read the flowchart and act on it. A flowchart for a brand-new help-desk hire on day one needs different boxes than a flowchart for a senior IT admin who already knows the system. The level of detail in your flowchart follows the audience — there is no single "correct" level for everyone.

### Reusable block

A chunk of process that shows up inside many larger processes. *"Log the user in"* is reusable: it appears in the help-desk ticket process, the new-device process, the first-day-at-school process, and dozens of others. A reusable block earns its keep when it appears in two or more processes — once is not enough.

### Named block / function (Week 3 informal sense)

A reusable block that has been given a short verb-phrase name and a one-sentence description of what it does. **Not a code function yet** — no parentheses, no return values, no parameters as named slots. In Week 3 a "function" is a labelled box in a flowchart with a verb-phrase inside (*"register a new device"*, *"reset a password"*) and a short English description of what the box does and what its input and output are.

### Input to a function (informal)

What the named block needs before it can run. *"Reset a password"* needs the username; *"register a new device"* needs the device's serial number and the user it belongs to. In Week 3 the input is one or two short sentences, not a typed list.

### Output of a function (informal)

What the named block produces when it is done. *"Reset a password"* produces a working new password and a record that the reset happened. *"Register a new device"* produces a device entry in the school's directory. The output is the reason the next box in the larger flowchart can run.

### Trade-off (in abstraction)

What you give up when you hide a detail. A named block ("register a new device") makes the larger flowchart readable — the reader is not drowning in twelve small boxes — but the reader who needs the detail must know where to look. Abstraction always has a trade-off; the question is whether the trade is right for the audience.

### Condition *(looking ahead — central topic of Week 5)*

The formal name for what the L7 decision diamond holds. In Week 3 we write the diamond as a plain-English yes/no question. In Week 5 the same diamond becomes a *condition* with formal language — *if / then / else*, *and / or* — and the same Yes/No arrows become the *then* and *else* branches. The shape stays; the words get sharper.
