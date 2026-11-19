# Lesson 11 — Criteria for evaluating solutions

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
