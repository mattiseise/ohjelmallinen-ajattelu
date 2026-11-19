# Lesson 3 — Precise and imprecise instructions

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
