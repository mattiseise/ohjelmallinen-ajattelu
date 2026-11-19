# More than one right answer — comparing solutions

## Introduction

Picture two friends, Maya and Jonas, making tea in the same kitchen on the same morning. Maya boils a kettle first, then drops a bag into her cup, then pours. Jonas drops a bag into his cup first, then boils the kettle, then pours. Both end up with a drinkable cup of tea. Neither is doing it wrong. They are doing the same task in two different orders.

That is the surprise this week sits on. The same problem — *make a drinkable cup of tea* — has more than one correct solution. They differ in the order of steps and in what each leaves to the user's judgement. Neither is the "right" one in the abstract.

Now picture two students walking home from school. One cuts through the park, the other takes the main road around it. Both reach home in roughly the same time. Two valid routes — and a quiet daily choice between them.

The central message of the week is one sentence:

> **More than one valid solution can solve the same problem. Picking between them is not a matter of taste — it is a matter of stated criteria.**

Week 4 is the **mid-course reflection week**. No new computational-thinking primitive is introduced. The raw material is what you already built in Weeks 1–3 — algorithms, decompositions and AT1, flowcharts and named blocks. What we add is a way of *looking* at that work. **Lesson 10** shows that *"correct"* is not unique. **Lesson 11** names the four working **criteria** — *clarity*, *efficiency*, *repeatability*, *error-proneness*. **Lesson 12** puts the criteria to work in a structured **peer-review and revision** protocol on a real artefact you made in Week 2 or Week 3.

Week 4 has no AT submission. **AT2 — the process description** is submitted at the end of Week 5 / during Week 6, and the peer-review-and-revision habit you train this week is exactly what AT2 expects. Keep your notes.

A practical note. We do **not** assign numeric scores to solutions in this course. The four criteria are *descriptive lenses*, not a 1-to-5 rubric. *"Recipe A is clearer at step 3 because…"* is the right shape. *"Recipe A scores 4/5 on clarity"* is not.

---

## Lesson 10 — Same problem, multiple solutions

### A problem is not the same as its solution

A **problem** is a goal stated in words: *make a drinkable cup of tea*, *get to school on time*, *have a recoverable backup of the project folder*. The problem says **what** you want; it does not say **how** to get there.

A **solution** is one way of reaching the goal — a specific sequence of steps a literal follower can carry out. Most interesting problems have more than one. Maya's tea and Jonas's tea are two solutions to the same problem. The park route and the main-road route are two solutions to *get home*.

A **valid solution** is one that actually reaches the goal. Validity is a yes/no property: either the tea is drinkable or it is not, either the backup is recoverable or it is not. Validity does not say *how well* the solution does the job — that is what the criteria in Lesson 11 are for.

The first move of the week is small but important. **Stop assuming there is one right answer.** Start expecting two or three valid solutions and start looking carefully at how they differ.

### Two valid solutions, side by side (everyday)

Two tea recipes. Same goal: a drinkable cup of tea.

| Step | Recipe A (boil first) | Recipe B (steep first) |
|------|------------------------|---------------------------|
| 1 | Fill the kettle with 250 ml of water | Put one tea bag into the cup |
| 2 | Boil the water | Fill the kettle with 250 ml of water |
| 3 | Put one tea bag into the cup | Boil the water |
| 4 | Pour the boiled water over the bag | Pour the boiled water over the bag |
| 5 | Wait 3 minutes, remove the bag | Wait until the colour looks right, remove the bag |

Both recipes are five steps. Both produce a drinkable cup of tea. They differ in two visible ways. First, the **order** of steps 1–3 — Recipe A boils before placing the bag, Recipe B places the bag before boiling. Second, the **stopping cue** at step 5 — Recipe A names a number (*3 minutes*), Recipe B names a colour judgement.

The first reaction is often *"so which one is right?"* — and the answer is *both*. The interesting question is not *which* is right but *how* they differ.

### Two valid solutions, side by side (IT)

Now the IT mirror. Two ways to back up the same project folder. Same goal: a recoverable copy of the folder.

| Step | Method A (USB copy) | Method B (zip + email to self) |
|------|----------------------|----------------------------------|
| 1 | Plug the USB drive into the laptop | Right-click the project folder |
| 2 | Open the project folder on the laptop | Choose *"Compress to .zip"* |
| 3 | Select all files (Ctrl+A) and press Ctrl+C | Wait for the zip file to appear next to the folder |
| 4 | Open the USB drive in the file manager | Open your school email and start a new message |
| 5 | Press Ctrl+V, wait for the copy to finish | Attach the zip file to the message |
| 6 | Eject the USB drive safely | Send the message to your own email address, save it in a *Backups* folder |

Both are six steps. Both produce a recoverable copy. They differ in where the copy lives (a physical USB drive vs. an email server), in what gets transferred (many files vs. one zip), and in what kinds of accidents the follower might have.

This is the **vocational angle for the week**. Real first-year ICT work includes deciding how to back up a folder of project files — there is no one official "right" way, and *which method to use today* is exactly the kind of question criteria help you answer.

### What is the same, what is different?

Across both pairs of examples, the same kinds of differences show up:

- **Step order** differs (boil first vs. bag first; copy files vs. zip first).
- **What is left to the follower** differs (three minutes vs. a colour; pressing Ctrl+V vs. attaching a file in an email).
- **What can go wrong** differs (pulling the bag too early vs. forgetting to eject the USB drive).
- **What happens when the input changes** differs (Recipe B's colour cue still works on a stronger tea; Method A on 500 small files behaves very differently from Method A on one big file).

None of these differences is an error. All of them are real. They are the **shape** of the comparison Lesson 11 will give you a vocabulary for.

> **Pause for a moment:** Pick one familiar task you do most days — making breakfast, getting ready for school, joining your first online class of the day. Write the steps two ways. Boil-first vs. steep-first. App-first vs. browser-first. Bag-on-back vs. bag-on-floor. Aim for two valid alternative procedures, each five to eight steps. Do not pick a winner yet — just notice that both work and that they are not the same.

---

## Lesson 11 — Criteria for evaluating solutions

### From taste to criterion

Here is what often happens when you show two valid solutions to a class. Someone says *"I just like the first one better."* Someone else says *"the second one is the right way."* A third person shrugs. None of these reactions tells anyone anything useful, because none of them names *what* makes one solution better at *what*. They are all taste.

A **criterion** is a stated yardstick that turns taste into reasoning. Instead of *"I like A better"*, you say *"A is clearer at step 5 because *3 minutes* tells the follower exactly when to stop."* That sentence names a property (*clarity*), points to a specific spot (*step 5*), and gives a concrete reason. It is a sentence someone can argue with — or agree with — on the basis of the artefact, not on the basis of how they feel today.

The central move of the week, written out once more:

> **More than one valid solution can solve the same problem. Picking between them is not a matter of taste — it is a matter of stated criteria.**

You move from *"I like this one better"* to *"this one is better at clarity"*. From *opinion* to *named property + specific spot*. That is the whole move.

### The four criteria for this course

For this course we work with **four** criteria. They are not the only criteria in the world — *cost*, *accessibility*, *security* exist in real IT life. Four is enough to train the habit. They appear in this fixed order on first mention: **clarity**, **efficiency**, **repeatability**, **error-proneness**.

**Clarity:** How easy the solution is to read once and act on without asking questions. A clear instruction names the right step, the right object and the right next move; an unclear one leaves the literal follower from Week 1 guessing. Everyday: *"add a tea bag"* is clearer than *"add the thing"*. IT: *"save the file as `2026-05-20_invoice.pdf` on the shared drive"* is clearer than *"save it where it should go"*.

**Efficiency:** How free the solution is of wasted steps. An efficient solution reaches the goal without detours, duplicates or rework — *no wasted steps*, not just *fast*. Everyday: heating the water once is more efficient than boiling, cooling, and reboiling. IT: zipping a folder once and uploading the zip is more efficient than uploading 500 files one at a time.

**Repeatability:** How reliably the solution produces the same result the second, third and tenth time, with the same input. A repeatable solution does not depend on the follower's mood, memory or guesswork. Everyday: a recipe that always uses 200 ml and one bag is more repeatable than *"a bit of water, taste it"*. IT: a backup that runs from a saved checklist is more repeatable than one that depends on remembering where the folder lives this month.

**Error-proneness:** How easy it is to do the *wrong* thing while following the solution. Low error-proneness means few foot-guns; high error-proneness means the next person down the line is one slip away from the wrong outcome. Everyday: *"pour the boiling water on the bag, then sit it for three minutes"* is less error-prone than *"pour the water on, count to a bit"*. IT: a backup that names the date in the filename is less error-prone than one that overwrites the same `backup.zip` every time.

A note on words. Some textbooks use *readability* for clarity, or *robustness* for low error-proneness. **In this course we keep the four names above**, in that fixed order on first mention.

### Applying the four criteria to the two tea recipes

Now back to the two tea recipes from Lesson 10, this time with the criteria as a lens.

| Criterion | Recipe A (boil first) | Recipe B (steep first) |
|---|---|---|
| **Clarity** | Step 5 names a number (3 minutes). A literal follower stops at the right time. | Step 5 names a colour the follower has to know. A new follower may stop too early or too late. |
| **Efficiency** | Five steps, one boil, one steep — no wasted steps. | Five steps, one boil, one steep — no wasted steps. |
| **Repeatability** | Same 200 ml and same 3 minutes → same drink Monday and Friday. | Same kettle, same colour-judgement → drink depends on the day's eye. |
| **Error-proneness** | Hard to go wrong if the follower has a watch. | Risk of pulling the bag too early or too late if the follower is new to tea. |

Read cell by cell. Recipe A is **clearer at step 5** because *3 minutes* tells the follower exactly when to stop. The two recipes are **equally efficient** — same number of steps. Recipe A is **more repeatable** because a clock is the same on Monday and Friday and a colour judgement is not. Recipe A is also **less error-prone** for a new follower; for a practised tea-drinker the difference shrinks.

Notice what the table does *not* do. It does not assign Recipe A a score of 4/5. It does not declare an overall winner. It walks one criterion at a time, says one concrete thing per cell, and stops there.

### Applying the four criteria to the two backup methods

Now the IT mirror. Two backup methods, four criteria.

| Criterion | Method A (USB copy) | Method B (zip + email to self) |
|---|---|---|
| **Clarity** | Each step names a concrete UI action (*plug in*, *select all*, *press Ctrl+V*, *eject*). | Each step names a concrete UI action (*right-click*, *Compress to .zip*, *attach*, *send to self*). |
| **Efficiency** | Many files copied one at a time — slow on a folder of small files. | One zip file is created and moved once — fewer wasted transfers. |
| **Repeatability** | If the USB drive is not plugged in, the procedure stops; the result depends on remembering the USB drive. | The email server is always available from school; same procedure works on any laptop. |
| **Error-proneness** | Easy to overwrite an old backup if the follower does not rename the destination folder. | Each email is dated automatically — a previous backup is hard to lose by accident. |

Read across, not down. The methods are roughly **equally clear** — both name concrete UI actions. Method B is **more efficient on a folder of many small files** (one zip transfer instead of many). Method B is **more repeatable across devices** (the email server is always there; the USB drive may not be). Method B is **less error-prone** for keeping old backups, because each email is dated and the old one is not overwritten.

This is one comparison, on this kind of folder. On a 50 GB folder of video files the picture changes — the zip step becomes slow and the email may not accept the attachment. **The comparison depends on the input.**

### Trade-offs — when criteria pull in different directions

A trade-off is a situation where two criteria pull in different directions, so improving one means giving up some of the other. Recipe B is **less clear at step 5** but is **just as efficient** as Recipe A and may be more pleasant for a practised tea-drinker. Method A is **simpler to explain** on day one (a USB drive is something you can hold) but Method B is **more efficient and more repeatable** for daily use.

Trade-offs are not a problem to solve — they are the *shape* of the comparison. The most common mistake is to declare a winner anyway. Resist that. **Name the trade-off.** *"Recipe A is clearer; Recipe B is faster for someone who knows what tea should look like. The right choice depends on whether the follower has done this before."* That sentence is the analysis.

A single solution does not have to win on every criterion. The four criteria are descriptive lenses, not a leaderboard.

> **Pause for a moment:** Pick your two L10 alternative procedures from the first Pause prompt above. Build a four-row table — one row per criterion. Fill in one short sentence per cell, naming a specific step where you can. You are not asked to pick a winner. Notice which criteria pull in opposite directions.

> **Pause for a moment:** Think about a piece of software you use most days — a chat app, a streaming service, the school portal. Pick one feature with two ways of using it (typing a search vs. clicking a category; the keyboard shortcut vs. the menu). Which way is clearer for a new user? Which is more efficient for a daily user? Which criterion does the developer probably care about more?

---

## Lesson 12 — Improving one's own solution and using peer feedback

### Why your own solution is the hardest to see clearly

In Week 1 you learned that a literal follower takes your instructions exactly as you wrote them. The trouble is that the literal follower **inside your own head** does not exist when you re-read your own work — your head knows what you meant and silently fills in any gaps. You read *"check the file"* and add *"the one in Downloads, dated today"* without noticing. A reader who is not you does not have that head-filler.

The four criteria are a way of reading your own work *with someone else's eyes*. By walking through clarity, efficiency, repeatability and error-proneness one at a time, you force yourself to ask the questions a stranger would ask. Even better: a real partner reading your artefact asks even sharper questions, because they actually cannot see what you meant. **That is what peer review is for.**

This lesson is the working lesson of the week. By the end of it you will have read a partner's artefact, written them two pieces of criterion-named feedback, received feedback in return, and **revised** one of your own existing Week 2 or Week 3 artefacts. No new artefact is created in Week 4.

### The peer-review protocol (criteria → feedback → revision)

The protocol is three steps, in this fixed order.

1. **The reviewer reads the partner's artefact silently.** Once through, without speaking, with the four criteria in mind. The reviewer then writes **one sentence per criterion** in the fixed order — clarity, efficiency, repeatability, error-proneness. Each sentence is either *"Strong on X because…"* or *"Could be improved on X because…"*, names the criterion, and points to a specific step or block.

2. **The reviewer hands back two pieces of feedback total** — not four. From the four sentences they wrote, they pick the *two most useful* and hand those to the author. Each names a criterion.

3. **The author then revises the artefact** to act on at least one of the two pieces of feedback. The revision is a change to the original — not a brand-new artefact, not a from-scratch rewrite. The author writes a 3–5 sentence **change note** naming what changed and which criterion drove the change.

That is the whole protocol. Two pieces of feedback in, one revision out, one change note that names the criterion. The shape stays the same in class with a partner, alone with your 24-hour-old self, and (in Week 5/6) inside AT2.

### Giving feedback that someone can actually use

Three short rules for any criterion-named feedback.

- **Always name the criterion.** *"This is unclear"* is taste in disguise. *"This is unclear at step 3 because the word *file* does not say which file"* is a sentence the author can act on.
- **One concrete spot, not a general impression.** *"The whole thing is too long"* is unactionable. *"Steps 4 and 5 repeat step 2"* points at a specific place.
- **A suggestion is optional but welcome.** *"Maybe combine steps 4 and 5 with the rest"* is helpful. It is fine to leave the *how* to the author; what matters is that the *what* is named.

And one rule that goes underneath all three: **critique the artefact, not the person.** *"This step is unclear"* is feedback. *"You are unclear"* is not.

### Receiving feedback you don't agree with

You are not obliged to act on every piece of feedback. You **are** obliged to consider it, and to be able to say which criterion it speaks to and why you don't think it applies here. *"My partner said step 3 is unclear, but step 3 names the exact file. The criterion of clarity is fine here."* That is a good reason to keep step 3 as it was — it is criterion-named and honest.

What you may not do is **defend** the artefact during the live Q&A. The Q&A is for **clarifying** the feedback (*"do you mean step 3 or step 4?"*), not for arguing. The decision to act on or reject a piece of feedback comes in the revision step, not in the exchange.

### Looking ahead to AT2

**AT2 — the process description** lands at the end of Week 5 / during Week 6. AT2 will ask you to describe a process in writing, hand it to a partner, receive feedback, and **revise it** before submission. That is exactly the cycle you trained in Week 4.

Keep two things from this week:

- The two pieces of criterion-named feedback you received on your Week 2 or Week 3 artefact.
- Your revision and the 3–5 sentence change note.

AT2 will ask you to **repeat the same cycle on a Week 5/6 artefact**. The vocabulary — *criterion*, *clarity*, *efficiency*, *repeatability*, *error-proneness*, *trade-off*, *revision* — is exactly what AT2 expects.

> **Pause for a moment:** Open your Week 2 decomposition (AT1) or your Week 3 flowchart now. Walk through the four criteria in your head — clarity first, then efficiency, then repeatability, then error-proneness — and write yourself one criterion-named comment for each. Then circle the two most useful ones. Those are the two pieces of feedback your 24-hour-old self would give you. Does any of them point at a specific step you could revise without starting over?

---

## Summary and what comes next

Week 4 added one habit on top of the artefacts you already had. You learned that the same problem can be solved by more than one valid procedure (L10), that four named criteria — **clarity, efficiency, repeatability, error-proneness** — turn taste into reasoning (L11), and that a structured peer-review-and-revision cycle on a real artefact you already made is the engine of improving your own work (L12). No new primitive. No code. No grades. Just a sharper way of looking at the work in front of you.

The central message of the week, one more time, verbatim:

> **More than one valid solution can solve the same problem. Picking between them is not a matter of taste — it is a matter of stated criteria.**

If you can name the four criteria, compare two short solutions criterion-by-criterion in writing, give a partner two criterion-named pieces of feedback, and revise one of your own artefacts with a 3–5 sentence change note, you have done the move Week 4 trained.

In **Week 5** the question changes again. Week 5 introduces **logic structures**: the L7 diamond becomes a formal **condition** (*if / then / else*) and a new primitive arrives — the **loop** (do, look, change, do again). The loop is also called *iteration*, and the peer-review-and-revision cycle you practised this week is its very first version. AT2 lands at the end of Week 5 / during Week 6. The notes you keep this week will be reused there.
