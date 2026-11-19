# Drawing the process — flowcharts, abstraction, and reusable blocks

## Introduction

You spent last week breaking a big task into smaller ones — main task, subtasks, sub-goals, dependencies. That work just left your hands as **AT1** at the start of this week. Open your AT1 notebook and look at the decomposition you wrote. You have a tree of small tasks. Now imagine handing the whole tree to a new colleague and walking away. What do you actually give them? A list of subtask names is not enough — there will be choices along the way. A flat list of every single step is too long for one page. You need something else: a picture.

The central message of the week is one sentence:

> *"Once you can decompose a problem, the next skill is to describe the process so someone else can run it — and to decide which details matter and which can be safely hidden."*

This week trains three closely linked moves. **Lesson 7** introduces the **simple flowchart** — the first picture in the course, built from four basic shapes. **Lesson 8** introduces **abstraction** — choosing what to leave out so the picture fits the audience. A bus stop on a city map is an abstraction; the "Save" button on your phone is an abstraction. **Lesson 9** introduces the informal idea of a **function** — a chunk of process that appears in many flowcharts, named once and reused everywhere. *"Log the user in"* is one. *"Register a new device"* is another. In Week 7 the same idea becomes a real JavaScript function. This week it is a labelled box and one sentence of plain English under it. No code yet.

The literal-follower mindset from Week 1 is still in force. Every box, every named block, every yes/no path is read by a follower who takes you at your word.

Week 3 has no AT submission. **AT2 — process description** is submitted at the end of Week 5 / during Week 6, and the flowchart vocabulary you build this week is exactly what AT2 expects.

---

## Lesson 7 — Describing a process and the simple flowchart

### When a list is not enough

Picture your morning routine on a normal school day. Alarm, get up, wash, dress, eat, bag, out the door. Seven steps in a flat list. A literal follower could carry this out without a single decision. The list works.

Now picture the same morning when something is off. *Did the alarm actually go off?* If it did, you have time for breakfast. If it did not, it is 8:10 already and you have to skip breakfast. *Is it raining?* If yes, bring an umbrella. *Is there milk in the fridge?* If yes, cereal; if no, toast.

The flat list cannot hold this. *Step 5 — eat breakfast* is now several different things depending on the answers to several different questions. By the time there are three or four questions in the process, the list becomes unreadable.

A flowchart is what a list becomes when the process has branches. A list says *do this, then this*. A flowchart says *do this, then ask this question, and depending on the answer go this way or that way*. The moment a process has a yes/no question in it, a flat list stops being enough.

The same shift happens on a help-desk. *"Did the user provide a screenshot?"* If yes, attach it and move on. If no, ask for one first. A flat list cannot draw that question. A flowchart can.

### The four shapes

A flowchart in this course uses exactly four shapes. Each one has one job.

- **Start / End (oval).** The oval that opens or closes the flowchart. Every flowchart has exactly one **Start** oval and at least one **End** oval. The Start oval says where the process begins; an End oval says where one path stops.
- **Step (rectangle).** A rectangle holds one action — *"Check the weather forecast"*, *"Save the file"*, *"Send the ticket to the user"*. One rectangle, one action. If a rectangle turns out to mean three different things, you either split it into three rectangles or hide them inside a named block (Lesson 9).
- **Decision (diamond).** A diamond holds one yes/no question — *"Is rain probability above 50%?"*, *"Does the file name match the convention?"*, *"Can the user log in?"*. A decision diamond has two outgoing arrows, one for each answer, and each arrow carries its own label (usually *Yes / No*).
- **Arrow / flow.** Arrows show the order in which the follower moves through the flowchart. Every shape has at least one outgoing arrow, except End ovals. Decision diamonds have exactly two.

Four shapes. That is the whole vocabulary of the picture. The skill of this lesson is not memorising more shapes; it is using these four well.

Here is a very small flowchart that uses all four. It is the morning umbrella decision, drawn as a process:

```
   ( Start )
       |
       v
[ Check the weather forecast ]
       |
       v
< Is rain probability > 50% ? >
   /                       \
  Yes                       No
   |                         |
   v                         v
[ Bring umbrella ]      [ Leave umbrella at door ]
   \                         /
    \                       /
     v                     v
       ( Leave the house )
```

Read it from the top. Start. Check the forecast. Ask the question in the diamond. If the answer is yes, bring the umbrella. If no, leave it at the door. Either way, leave the house. The flowchart has one Start oval, one End oval, two rectangles before the diamond and one after on each path. Eight shapes. The branch is the whole reason this is a flowchart and not a list.

### Reading a flowchart

Reading a flowchart is following the arrows. You start at the Start oval. At each rectangle, you do what it says. At each diamond, you ask the question and take the arrow whose label matches the answer. You stop when you reach an End oval.

Try the umbrella flowchart with a worked answer. The forecast says 70% probability of rain. *Start.* Check the forecast. Hit the diamond and ask *"is rain probability > 50%?"* — yes, 70% is above 50%. Take the Yes arrow. Bring the umbrella. Leave the house. One run through the process.

Now imagine the forecast says 20%. Same flowchart, the No arrow this time, umbrella stays at the door. Two valid runs, both ending at the same End oval. That is what a branch buys you.

A flowchart is correct when **every path** through it lands at an End oval. An arrow that goes off the page leaves the follower stuck.

### Drawing your first flowchart

Pick one familiar process from your own life that has at least one yes/no question in it: *"should I bring an umbrella?"*, *"should I take the bus or walk?"*, *"which charger fits this device?"*, *"should I save this file with the date in the name?"*. Pick one where the answer changes depending on the day.

On paper or on a tablet, draw the four shapes in pencil. Start oval at the top. Rectangles for the actions you always do. A diamond where you have to make a yes/no decision. Two arrows out of the diamond, each labelled. Rectangles on each branch. End oval (or two, if the branches end in different places). Maximum eight shapes — if you need more, the level of detail is too low and Lesson 8 will help.

Once it is drawn, follow it with your eyes from Start to End on each branch. Did you actually do what the flowchart says, this morning? If yes, the flowchart is honest. If no, fix the flowchart — not your morning.

This is the work of **Task 3.1**. Draw the flowchart, sign and date it, and keep a photo of it for your AT2 notes.

> **Pause for a moment:** Look at your morning so far today. Was there a moment when you made a yes/no decision without thinking about it (umbrella, bus or walk, hot or cold drink)? Could you describe that decision as a single diamond with two arrows out of it? What did the two arrows actually do today?

### IT examples

Two short IT processes drawn as flowcharts.

**Help-desk triage.** A user opens a ticket saying *"I can't log in"*. The first-line agent has to decide what to do next.

```
   ( Start — ticket received )
        |
        v
[ Read the ticket text ]
        |
        v
< Can the user log in now? >
   /                     \
  Yes                     No
   |                       |
   v                       v
[ Close the ticket ]    [ Ask the user for a screenshot ]
   |                       |
   v                       v
( Closed )              ( Wait for reply )
```

One decision diamond, two paths, two different End ovals. *"Can the user log in now?"* honestly leads to two outcomes.

**File-naming check.** Before saving a document to the shared drive, the school's convention says the file must be named like `2026-05-20_invoice-001.pdf`.

```
   ( Start )
       |
       v
[ Look at the file name ]
       |
       v
< Does the file name match the convention? >
   /                              \
  Match                           No match
   |                                |
   v                                v
[ Save to shared drive ]      [ Rename the file first ]
   |                                |
   v                                v
( Saved )                       [ Save to shared drive ]
                                    |
                                    v
                                ( Saved )
```

Notice two things. The branch labels are *Match / No match* — the rule is *each branch has a short label*, and *Match* reads more clearly than *Yes* here. Both branches eventually reach a *Saved* End oval, but the No-match path has an extra step.

> **Pause for a moment:** Pick one IT task you have actually done — installing an app, sharing a file, joining a video call. Is there a yes/no question hiding inside it that you do without thinking? What would the diamond look like?

---

## Lesson 8 — Abstraction

### What "abstraction" means here

When you drew your flowchart, you made a choice on every rectangle. *"Check the weather forecast"* is one box. It could just as well have been four: *"Open the weather app → read today's forecast → look at the rain probability → close the app"*. Both describe the same action. You drew one box instead of four. **That choice is abstraction.**

Abstraction is the move of **hiding the detail that does not matter at the level you are describing**. The boxes you do draw stay precise; you just choose not to draw the boxes that would not help the reader at this level. Abstraction is not vagueness — *"check the weather"* is precise about *what* the follower does. It just hides *how*.

A small everyday example. Picture a city bus stop — say, Park Street bus stop, the one near your school. To a passenger waiting for the bus, the bus stop is a sign saying "Park Street" and a timetable underneath. That is the abstraction the passenger needs. To the bus dispatcher in the city's control room, the same bus stop is a GPS coordinate, an ID number in a database, and a list of buses due in the next twenty minutes. To the engineer who replaces the timetable display, it is an electrical junction box and a set of screws. Same physical thing. Three abstractions, each right for a different audience.

That is what abstraction is here: choosing what to leave out so the description fits the audience.

### A "Login" button is an abstraction

Now an IT example. Open your school's portal and look at the *Login* button. Three letters of text and a coloured rectangle.

What is hidden inside it? When you press the button, the page sends your username and password to the school's identity server. The server checks the password against a stored, encrypted version. If the check passes, the server sends back a *cookie* the browser stores; every page you visit after that includes the cookie, so the system knows it is still you. If the school signs in through Microsoft or Google, there is also a back-and-forth between three servers called the OAuth dance, all happening while the spinning circle is still on screen.

That is the abstraction the Login button buys you. The button means *"sign in to the portal"*. You do not see the identity server, the password check, the cookie, or the OAuth dance. They are **hidden** — still there, but not on the button. The button is the right description *for the user*.

Now picture the same button as it appears to a security engineer debugging a failed sign-in. *Login* is not enough there; the engineer needs the request, the response, the cookie, the timestamps. Same button. Two audiences. Two right answers.

### Level of detail follows the audience

Here is the rule of thumb that holds the lesson together. **The right level of detail follows the audience.**

Before you decide *which boxes to draw*, ask *who is going to read this and what will they do with it?*

A flowchart of the file-naming check for a brand-new help-desk hire on day one needs more rectangles — *"open the file-naming-rules document"*, *"look up the current convention"*, *"check each part of the name"*. Maybe six rectangles before the diamond.

A flowchart of the same check for a senior IT admin who has been there ten years has one rectangle: *"Read the file name"*. Same process, same goal, different audience, different level of detail. Both are correct. The question *"what is the right level of detail?"* has no universal answer — only an answer *for this audience*.

### Hiding vs. forgetting

Abstraction is **hiding** a detail, and hiding is not the same as **forgetting**.

A small everyday example. Your morning routine flowchart has a rectangle that says *"Get dressed"*. You have hidden a lot of detail in that rectangle — which clothes, what order. None of it is on the flowchart, but you have not forgotten any of it. If your little cousin asks *"what does 'get dressed' mean?"* you can open the rectangle in your head and answer. The detail is still there. It is **filed**, not deleted.

Forgetting is when you write *"get dressed"* and have no idea what it means any more. The literal follower opens the box and finds nothing inside.

The IT version. The Login button hides the OAuth dance. The engineer who set up the school portal three years ago has the OAuth steps written down in a runbook somewhere. The hidden detail is filed. *Hidden* means there is a place to look. *Forgotten* means there isn't.

The trade-off in one sentence: a good abstraction hides what does not help the reader at this level, **and points to where the detail is filed** for readers who do need it.

> **Pause for a moment:** Pick one button, link, or menu item in software you actually use — Discord's "Send", Spotify's "Play", your phone's "Take photo", the school portal's "Submit". List three things that are hidden inside it when you press it. Are those three things hidden (filed somewhere) or forgotten? How would you find out which?

> **Pause for a moment:** Take your Task 3.1 flowchart from Lesson 7. Pick one rectangle. Is the level of detail in that rectangle right for *you, drawing your own morning*, or is it really right for *someone else* who would read it? If it is the wrong audience, would you draw the rectangle differently for the right one?

---

## Lesson 9 — Reusable instructions: the idea of a function without code

### When the same chunk keeps reappearing

Look at two flowcharts side by side.

The first is *"first day at a new school"*. Somewhere in the middle there is a chunk: *Open the school portal → enter username → enter password → press Login → wait for landing page*. Five rectangles.

The second is *"submit an assignment online"*. Near the start, the same chunk appears: *Open the school portal → enter username → enter password → press Login → wait for landing page*.

You could keep drawing it every time. By the third flowchart your hand is tired and the page is full before you reach the interesting part. There is a better move. **Give the chunk a name.**

### Give the chunk a name

The name is a short verb-phrase that says *what the chunk does*, not *how it does it*. For the chunk above, the name is *"log the user in"*. Three words. The whole chunk in a verb-phrase.

A good name passes a simple test. Someone who has never seen the original five rectangles can read *"log the user in"* and know what to expect: at the end of this box, the user is logged in. They do not know *how* — that is hidden. But they know *what*, and they know *when the box is done*.

More names from the everyday and IT worlds: *"rename the file"*, *"back up the device"*, *"reset a password"*, *"register a new device"*, *"send a notification to the parent"*. Each is a verb-phrase that says what happens.

A bad name fails the test. *"Do the thing"* tells nobody anything. *"Step 7"* is just a number. The rule is *verb-phrase that says what it does*.

Now the second flowchart with the named block in place of five rectangles:

```
   ( Start — student wants to submit assignment )
        |
        v
[ log the user in ]   <-- one named block, not five rectangles
        |
        v
[ Find the assignment in the course list ]
        |
        v
[ Upload the file ]
        |
        v
[ Click submit ]
        |
        v
( Submitted )
```

Five flowchart shapes total. The original would have been nine. The flowchart fits on the page, the reader sees the interesting part clearly, and *"log the user in"* still contains all five original steps — they just live in a separate description below the flowchart.

### What a "function" means in this week's sense

In Week 3, a **function** is informally defined as **a named, reusable chunk of process, described in plain English, with a clear input and a clear output**. Five things to keep in your head:

- **Named** — a short verb-phrase name.
- **Reusable** — appears in more than one larger process.
- **Chunk of process** — some steps grouped together, usually 3 to 8.
- **Plain English description** — a short paragraph of what the chunk does.
- **Input and output** — what it needs to start, and what it produces when done.

For *"log the user in"*:

> **log the user in** — Takes the user from a not-signed-in state to a signed-in state. The user opens the portal, types their username and password, presses Login, and waits for the landing page.
> **Input:** the user has a valid username and password.
> **Output:** the user is signed in and the portal landing page is on screen.

That is the whole "function" in Week 3 sense. **No code, no parentheses, no return values.** That all comes in Week 7. This week, a function is a labelled box on a flowchart and a paragraph underneath.

A second example:

> **rename the file to the school convention** — Takes a file with any name and produces a file whose name follows the school's date-and-topic convention.
> **Input:** the file exists; the user knows the date and a one-word topic.
> **Output:** the file has a name of the form `YYYY-MM-DD_topic.ext`.

Each named block has a clear input, a clear output, and a one-paragraph description. AT2 will ask you to write this shape — so it is worth practising now.

### Vocational example — "register a new device"

The IT example to lean on this week is **"register a new device"**. Every time a new laptop, projector, or conference-room display arrives at the school, somebody runs the same chunk: sticker with serial number, entry in the device directory, install the standard software set, check the network. About eight steps, every time, for every new device.

A flowchart for *"set up a new conference room"* without the named block:

```
( Start ) → [ Order the display ] → [ Receive the display ] → [ Sticker with serial number ]
   → [ Add entry to device directory ] → [ Install standard software ] → [ Check network ]
   → [ Mount on the wall ] → [ Run the cable to the laptop dock ] → [ Test with a test laptop ]
   → ( Done )
```

Ten boxes. Half are "register the device" steps. The IT manager who cares about the conference room has to scan five register-the-device boxes before reaching the interesting bit.

The same flowchart with the named block:

```
( Start ) → [ Order the display ] → [ Receive the display ] → [ register a new device ]
   → [ Mount on the wall ] → [ Run the cable to the laptop dock ] → [ Test with a test laptop ]
   → ( Done )
```

Seven boxes. The named block carries the five hidden steps. The hidden steps still exist — they live in the "register a new device" description, filed in the school's IT handbook for the trainee who actually has to run that block.

### The trade-off in one sentence

A named block **hides detail** so readers at this level do not drown, **but the reader who needs the detail has to know where to look**. Abstraction in Lesson 8 was about *which boxes deserve to be drawn*; named blocks in Lesson 9 are the same move at a higher zoom level — one box that stands for a whole sub-flowchart.

Bridge to Week 7. There, *"log the user in"* will become a real JavaScript function. The verb-phrase becomes the function name; the plain-English input and output become parameters and return values; the chunk becomes code. But the *shape* — a named, reusable chunk with an input and an output — is what you build this week, in English, in pencil.

> **Pause for a moment:** Look at your Task 3.1 flowchart and any other flowchart you have drawn this week. Is there a chunk of three or four boxes that you suspect would also appear in a different process you do? Write a verb-phrase name for it now, before you read on.

---

## Summary and what comes next

Week 3 added one move on top of Week 2's decomposition. You learned to describe a task as a flowchart with four shapes, to choose the right level of detail for the audience, and to spot chunks of process that reappear and give them reusable names. The literal-follower mindset from Week 1 still holds on every box: each rectangle says one thing, each diamond asks one question, each arrow goes one place.

The central message of the week, one more time, verbatim:

> *"Once you can decompose a problem, the next skill is to describe the process so someone else can run it — and to decide which details matter and which can be safely hidden."*

If you can draw a small flowchart, choose a level of detail for an audience, and name one reusable chunk, you have done the move Week 3 trained.

In **Week 4** the question changes. So far you have written *one* good description of a process. Week 4 asks: *what if there is more than one valid flowchart for the same goal?* You will draw two valid flowcharts for the same task, compare them with simple criteria, and practise peer feedback.

Keep your Task 3.1 flowchart, your named-block notes, and your abstraction reflections. This week's vocabulary — *flowchart*, *decision*, *abstraction*, *level of detail*, *reusable block*, *named block / function* — is exactly what **AT2 — process description** expects at the end of Week 5 / during Week 6.
