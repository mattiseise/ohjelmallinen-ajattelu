# Speaking to a computer — what does it actually hear?

## Introduction

Imagine your eight-year-old cousin walks into the kitchen and you tell her, "Make me a sandwich." She stares at you. There is bread on the counter, butter in the fridge, cheese somewhere, and a knife in a drawer she is not allowed to open. She has done this with her dad a hundred times, but right now, on her own, she does not know which bread, how thick, with or without crust, and whether the cheese counts. So she takes a slice of bread out of the bag, hands it to you, and asks, "Is this a sandwich?"

She is not confused about what a sandwich is. You just did not give her enough to go on.

This week is about that gap — the small distance between what you mean and what someone else hears. A computer lives in that gap permanently. It does not guess what you meant; it does what you wrote. The whole course you are about to start is built on a single question, and we will come back to it many times:

**How do I speak to a computer so that it understands what I want it to do?**

The first answer is not "learn a programming language." That comes later in the course. The first answer is: get used to saying *exactly* what you mean. By the end of this week you will be able to write a clear, step-by-step everyday instruction, hand it to a literal follower, see where it breaks, and fix it. No code, no special tools. Just careful sentences and a willingness to be wrong about how clear you thought you were.

---

## Lesson 1 — Speaking to a computer (literal interpretation and ambiguity)

### What is computational thinking?

Computational thinking is the everyday habit of breaking a task down into small, clear, ordered steps that a literal follower can carry out without guessing. It is the thinking *behind* programming, not programming itself. You are doing it every time you write directions for someone else: "Turn left at the bus stop, walk two blocks, the door is red." Whether the follower is a human or a machine, the same skill applies.

People who study this idea usually name four pillars: **decomposition** (breaking a big problem into smaller ones), **pattern recognition** (noticing what repeats), **abstraction** (focusing on what matters and ignoring the rest), and **algorithms** (the step-by-step instructions themselves). Each of these gets its own week later in the course. For now, hold on to one short version: *computational thinking is the habit of being clear, in steps, for a literal follower.*

This is also a good moment to clear up a common confusion. Computational thinking is **not** the same as programming. Programming is one place you use computational thinking. You can write a perfectly clear algorithm for boiling an egg without touching a keyboard, and the skill you used to do it is exactly the one a programmer uses. The keyboard part comes last.

### A computer takes you literally

Let us start away from computers entirely.

**Example 1 — the sandwich.** You ask your little cousin to make a sandwich. She is willing, she is paying attention, and she trusts you. But she has never made one alone. You said "make me a sandwich" — you did not say which bread, how many slices, what to put inside, or whether to cut it in half. She does the first thing that fits the words you actually said: hands you a slice of bread. She is following you literally. The bread is not a misunderstanding of "sandwich"; it is the part of "sandwich" she was sure about.

**Example 2 — the big tree.** A friend who has never been to your neighbourhood asks how to get to your house. You say, "Walk down my street, turn at the big tree, and it's the third door on the left." Three weeks later she tells you she got lost. Why? Because to you "the big tree" is obvious — it is the one on the corner with the white trunk — but to her every tree on that street looked roughly the same size. "Big" was not a measurement; it was a memory you had and she didn't.

Now the IT side.

**Example 3 — the typo search.** You want a Python tutorial and you type `pyhton tutorial` into a search engine. The search engine does not say "I think you mean Python." (Modern ones do, because they have been trained to guess, but the raw matching layer underneath does not.) At the literal level, it is looking for pages that contain `pyhton`, a word that does not exist, and gives you whatever comes closest. It is doing exactly what you typed.

**Example 4 — the missing slash.** A program tries to open a file at `Users/maria/documentsreport.txt` instead of `Users/maria/documents/report.txt`. To you the difference is one slash; to the computer it is the difference between a folder it can find and a filename it has never heard of. It does not try harder; it reports an error.

In all four examples there is no machine that is broken and no follower at fault. There is an instruction, and the instruction was less clear than the speaker thought.

### Ambiguity is in the instruction, not the computer

This is the conceptual pivot of the whole week, so it is worth saying slowly: **ambiguity is a property of the instruction, not of the follower.** When your cousin handed you a slice of bread, the ambiguity was in "make me a sandwich." When your friend got lost, the ambiguity was in "the big tree." When the search engine returned junk for `pyhton`, the ambiguity was in the typed word.

This matters because the cultural reflex is the opposite. When an instruction fails, people often blame the machine and say it does not understand them. That framing is wrong, and once you let go of it, the whole course gets easier. The computer is **literal**. It does exactly what is written, and that is actually its strength — if you can write a clear instruction, you can rely on the computer to follow it the same way every time.

So when something goes wrong, the question you learn to ask is not "why is this machine not getting it?" but "where in my instruction was I unclear?" That second question has answers. The first one does not.

### Why this matters for an IT professional

You might be wondering why a first-year vocational ICT student needs to think about sandwiches and trees. Here is the short version: an IT professional spends most of their day writing instructions. Instructions for machines (when you eventually write code). Instructions for colleagues (a ticket, a handover note, a step-by-step fix). Instructions for end users (a how-to guide, a chat-bot response, a help-desk reply, a README). All of these have the same shape, and all of them break in the same way: a word that seems obvious to you turns out to be unclear to the person on the other side.

When a customer writes "it doesn't work" in a support ticket, they are giving you an unclear instruction. When you write back "have you tried restarting?" without saying *what* to restart, you are giving them one. The whole field runs on small clear sentences, and the people who write them well stand out fast.

> **Pause for a moment:** Think of one time this week when you gave a clear instruction to a friend, a sibling, or a parent — and one time when you gave an unclear one. What was the difference? Was it a missing word, an assumption you made about what they already knew, or a number you did not specify?

---

## Lesson 2 — Algorithms in everyday life

### What is an algorithm?

An **algorithm** is a clear sequence of literal steps that takes you from where you are to a goal. That is the whole definition. It does not have to involve a computer. It does not have to be long. It does not have to use any special words. A grandmother's recipe written on a card is an algorithm. The mental checklist you go through when you leave the house is an algorithm. The route your bus takes is an algorithm. If a literal follower can carry out the steps and reach the goal, you have an algorithm.

The word sounds technical because we usually hear it next to "algorithm change at YouTube" or "TikTok's algorithm decided." Those algorithms are made of code and are very large, but they are still, at root, sequences of clear steps. The algorithm you are about to write yourself is the same thing, just shorter.

### Algorithms you already use

Here are three algorithms you almost certainly run every day without thinking of them that way.

**A recipe — tea with milk.** Goal: a hot mug of tea with milk. Input: a tea bag, water, milk, sugar (optional), a mug, a kettle. Steps: fill the kettle with cold water, switch the kettle on, put a tea bag in the mug, wait for the kettle to boil, pour the water into the mug over the tea bag, wait three minutes, take the tea bag out, add a splash of milk, add sugar if you want, stir. Output: a hot mug of tea with milk.

Notice four things in that recipe: a **goal** (what you are trying to end up with), an **input** (what you start with), a sequence of **steps**, and an **output** (what you actually get when the algorithm finishes). Almost every algorithm you meet — everyday or in IT — has these four parts.

**A route — home to school.** Goal: arrive at school on time. Input: you, your bag, your bus card, the time on the kitchen clock, your front door. Steps: leave the house by 7:50, walk to the bus stop on Park Street, take bus 12 in the direction of the city centre, get off at the stop called Market, walk two blocks east, enter through the main gate. Output: you, inside school, on time.

**A morning routine.** Goal: leave the house ready for the day. Input: you, asleep, in bed; an alarm; clothes; breakfast in the kitchen. Steps: alarm goes off, switch it off, get out of bed, shower, get dressed, eat breakfast, brush teeth, pack bag, put on shoes, leave. Output: you, dressed, fed, on the way out.

None of these are written in code. They do not need to be. They are still algorithms because each of them describes a clear sequence of literal steps from a known input to a known output.

The same shape appears in an IT context too. Picture the first-line help-desk script for "the user cannot log in." Goal: get the user logged in. Input: the username, the error message they saw, the computer they are on. Steps: ask the user to type their username slowly while you watch, check whether caps lock is on, ask them to try once more, if it still fails reset their password, send the new one to their personal email, ask them to log in with the new password, ask them to change it on first login. Output: a logged-in user and a closed ticket. Same shape: goal, input, steps, output.

> **Pause for a moment:** Look at the morning-routine algorithm above. If you had to give it to a literal follower — a robot vacuum cleaner with arms, say — which step would break first? Is it "get out of bed"? "Shower"? "Pack bag"? Pick one and write down, in one sentence, why a literal follower would get stuck there.

### Two algorithms for the same goal

A common mistake when people first meet the word "algorithm" is to think there is one correct algorithm per goal, and your job is to find it. Not true. For most everyday goals there are several valid algorithms, and all of them work.

Take the tea recipe again. Some people put the milk in first and pour the hot water on top. Some people put the milk in last, after the bag has steeped. Both end with a hot mug of tea with milk in it. Both are correct. They are different algorithms for the same goal.

Or take the route from home to school. You can walk to the bus stop on Park Street and take bus 12. Or you can walk fifteen extra minutes and take the tram instead. Or, on a sunny day, you can cycle. Three different algorithms, same goal: you, inside school, on time.

This matters because later in the course we will start asking, "is one of these algorithms *better* than another?" — and to ask that question you first have to accept that more than one of them can be valid. For now: notice when you and a friend solve the same everyday problem differently. You both have working algorithms. Neither of you is wrong.

### Writing your first algorithm in plain English

Before you read on, try this. On a piece of paper or in a notes app, write out the algorithm you follow when you make a cup of tea, or get yourself ready in the morning, or send a Discord message to a friend. Use plain English. Number the steps. Try to write between five and ten steps. Before you start, write the goal at the top. Before the steps, write what you start with (the input). After the steps, write what you end up with (the output).

If you find yourself writing a step like "do the usual thing with the kettle," stop and break it into smaller, more literal steps. A literal follower does not know what "the usual thing" is.

This is the same activity you will turn into Task 1.1 of the week's tasks. Do not worry about being elegant. Worry about being clear.

> **Pause for a moment:** When you wrote your steps, were there any places where you almost wrote a word like "usually," "normally," "the right one," or "the one you always use"? Those words are warning lights. A literal follower has no "usually." Circle them.

---

## Lesson 3 — Precise and imprecise instructions

### What does "imprecise" mean here?

An **imprecise** (or **ambiguous**) instruction is one that more than one literal follower could carry out in more than one way and still believe they followed it. Notice that the definition does not say anything about length. A very short instruction can be perfectly clear ("close the door"). A very long one can be hopelessly unclear if it keeps using vague words.

Here is a short instruction. Read it once and ask yourself how many different things a literal follower might do with it: *"Save the file in the usual place."*

What is "the file"? The one you have open? The one you were just looking at five minutes ago? The one your colleague mentioned in the chat? What is "the usual place"? Your desktop? The shared drive? The folder called `inbox` that you keep meaning to clean out? Six words and several possible meanings.

A clearer version might be: *"Save the file `report-may.docx` (currently open in Word) into the shared drive folder `Team/Reports/2026/May`."* The new version is longer, but it leaves only one thing for the follower to do.

### Hunting ambiguity

Ambiguity in everyday English tends to come in a few recognisable shapes. Once you know what to look for, you start spotting it everywhere.

**Vague nouns.** "Pass me the thing." "Open the file." "Reply to the email." In each of these, the noun (*thing, file, email*) is not specific enough to point at one object. Fix: name the object directly, or describe it in a way only one object fits.

**Deictic words** (words that depend on where the speaker is). "Put it here." "Take that over there." "Send it to him." *Here, there, it, him* all depend on context that the follower may not share. Fix: replace the deictic word with the actual location, object or person.

**Relative time.** "Run the script after lunch." "I'll do it later." "Send it soon." *After lunch, later, soon* mean different things to different people and on different days. Fix: name a specific time, or a specific event with no ambiguity ("after the 14:00 stand-up").

**Vague quantities.** "Add a bit of milk." "Make the button a bit bigger." "Reply to a few of them." *A bit, some, a few* are ranges, not numbers. Fix: give a number, a measurement, or a clear cap ("add 30 ml of milk," "make the button 24 pixels tall," "reply to the first three").

The same four patterns show up in IT contexts almost word for word. *Vague nouns:* "save it in the folder" (which folder?). *Deictic:* "log in here" (here on which page?). *Relative time:* "the deployment will go out later today" (before or after the 16:00 demo?). *Vague quantities:* "the upload is taking a while" (a minute? an hour?).

When you are reading an instruction someone else wrote — or one you wrote yourself five minutes ago — going through these four patterns in your head is one of the fastest ambiguity hunts you can do.

### Testing instructions by acting as the literal computer

There is one technique that beats every other technique for finding ambiguity in your own instruction: **test it by acting as the literal follower.**

Reading your own instruction is not enough. When you wrote it, you knew what you meant. So when you read it back, you read what you meant, not what you wrote. Your brain fills in the missing words automatically. The only way to break that habit is to follow the instruction one step at a time, with no memory of what you meant, the way a robot would. At each step, you ask: "Could I do this in more than one way? Did the previous step give me what I need to do this one?"

This is what Task 1.1 of the week's tasks is about. In Task 1.1 you write an instruction, hand it to a real follower, and watch them get stuck. In the in-class "literal robot" exercise (Lesson 3, second half) you do this live with a classmate playing the literal computer.

When you do this for the first time, you will be surprised. Instructions you were sure were clear turn out to have three or four spots where the follower has to guess. That is normal. Every IT professional discovers it the first time they write a how-to guide for a real user. The fix is never to write a longer instruction; it is to write a more *literal* one.

### Edge cases (a gentle introduction)

An instruction can be perfectly clear for the common case and still break in an unusual one. The unusual situation is called an **edge case**.

Take a tiny instruction: *"Open the fridge and take out the milk."* If there is milk in the fridge, the instruction works. But what if there is no milk? What if there are two cartons and one is past its date? What if the carton is in the door instead of on the shelf? These are edge cases. They do not mean the instruction is bad. They mean the instruction does not say what to do when the world is not in the shape the writer expected.

A more robust version might say: *"Open the fridge. If there is a carton of milk on the shelf, take it out. If there is more than one, take the one with the earliest date. If there is none, tell me."*

You do not need to anticipate every edge case in Week 1. You just need to start noticing that they exist. Later in the course (especially in Week 5, when you meet "if/then/else" thinking), you will learn to handle them on purpose. For now, when you write an algorithm, ask yourself once: "What if the world is not in the shape I expected? What would my follower do then?"

> **Pause for a moment:** Pick the morning-routine algorithm you wrote (or were going to write) in Lesson 2. Find one edge case — a situation where one of the steps would not work as written. (No clothes you like? No hot water? Alarm did not go off?) Write down, in one sentence, what your follower should do in that situation.

---

## Summary and what comes next

You started this week with a question: **How do I speak to a computer so that it understands what I want it to do?** You now have a first answer in three parts.

First, **a computer follows instructions literally.** The computer is exact, not creative. When something goes wrong, the question is not what is wrong with the machine, but where you were unclear.

Second, **an algorithm is the everyday name for a clear sequence of literal steps.** You use algorithms every day without thinking. The skill you will spend this course developing is the skill of writing algorithms that a literal follower can actually carry out.

Third, **instructions are not finished when they sound right.** They are finished when a literal follower can execute them without asking questions. Testing your instruction — by handing it to a real follower, or by acting as the literal follower yourself — is the only reliable way to find the unclear parts.

In **Week 2** we will keep the literal-follower mindset but tackle a new problem: what do you do when the task is too big to fit in a single algorithm? The answer is **decomposition** — breaking a problem into smaller problems you can solve one at a time. The instructions you have written this week have been small enough that decomposition has not been needed. Next week they get bigger.

Keep your notes from this week's tasks. You will reuse them, especially in the first assessed task at the end of Week 2.
