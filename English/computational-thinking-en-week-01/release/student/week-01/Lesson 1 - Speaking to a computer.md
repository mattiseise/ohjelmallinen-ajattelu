# Lesson 1 — Speaking to a computer (literal interpretation and ambiguity)

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
