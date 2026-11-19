# Speaking to a computer — what does it actually hear?

## Introduction

You ask a friend to "grab my charger from the kitchen table." Your friend walks in, sees three chargers on the table, picks up the wrong one, and brings it to you. You sigh and explain which one. Your friend was paying attention; the instruction was just not specific enough. Now imagine the same situation with a computer, except the computer cannot sigh and cannot guess. It just does what you wrote.

This is the question this whole course turns around: **How do I speak to a computer so that it understands what I want it to do?** It sounds simple. It is not. Most of the difficulty in programming, in writing a clear ticket, and even in giving a teammate good instructions comes from one fact: a computer reads what you wrote, not what you meant.

After this lesson you will be able to define computational thinking in your own words. You will be able to explain what it means to say a computer "takes you literally". You will be able to give an everyday example and an IT example of an instruction going wrong because of ambiguity, and you will see that the fault sits in the instruction, not in the machine.

## What is computational thinking?

Computational thinking is a way of thinking about problems so that a computer — or anyone following instructions literally — can solve them. It is the thinking *behind* programming. It is the part you do before you touch any code. When a baker writes a recipe so that a beginner can follow it without asking questions, that baker is doing computational thinking. When a help-desk worker writes a clear ticket so a colleague in a different time zone can fix the issue without a meeting, that is computational thinking too.

People who study this field often talk about four "pillars" of computational thinking: decomposition, pattern recognition, abstraction, and algorithms. Each of these gets its own lesson later in the course, so do not try to memorise them now. For Lesson 1, only one idea matters: the computer will do what your instruction actually says.

> **Pause for a moment:** Think of an instruction you gave today — to a friend, a sibling, a teacher, a chat bot. Did the other person do exactly what you meant? If not, was the problem in their head, or in your words?

## A computer takes you literally

Imagine you tell your little brother, "Make me a sandwich. Put the cheese between two slices of bread." He brings back two slices of bread balanced on top of a block of cheese. From his point of view, the cheese is between the slices: one slice is above the cheese, one is below. You meant the cheese on the inside, sandwich-style. He read the words the way they were written.

Or imagine you give a visitor directions to the city library. You say, "Turn left at the big tree." There are three big trees on that street. The visitor stops at the first one, turns left, and ends up at a car park. The directions were not wrong on purpose. They were just open to more than one reading.

A computer behaves like that little brother and that visitor, every time, with no exceptions. It cannot pick the "obvious" reading because it does not know which reading is obvious to you. It reads the instruction and does that thing.

The same pattern shows up the moment you start using IT tools. You type `pyhton tutorial` into a search box because you are in a hurry. The search engine looks for pages about `pyhton`, finds almost nothing useful, and returns a thin set of results — maybe even a polite "Did you mean: python tutorial?" The search did not fail; it did exactly what you asked. The typo was in your instruction.

Or you tell a program to open the file `report-final.docx` and the program says *file not found*. You stare at the screen, sure the file is there. It is — but it is in a folder you forgot you moved it to last week. The path you gave is wrong. The program is not lying. It looked exactly where you pointed it, and there was no file there.

> **Pause for a moment:** When an app does "the wrong thing", is it broken, or did it follow your instruction exactly? How would you tell the difference?

## Ambiguity lives in the instruction, not in the computer

A lot of people, when an app behaves in an annoying way, say things like "this computer is so dumb" or "this thing has no idea what I want." It is a normal reaction. It is also the wrong picture of what is happening.

The computer is not dumb. The computer is *literal*. Those are different things. A dumb listener cannot understand even a clear instruction. A literal listener understands the instruction word for word and does exactly what those words say. If the words can mean two things, a literal listener will pick one of them, and you do not always get to choose which.

This is the conceptual pivot of the lesson, and it is worth saying slowly: when a computer "does the wrong thing", the bug is almost always in the *instruction*, not in the *interpreter*. Ambiguity is a property of what you wrote, the way weight is a property of a backpack. The backpack is not lazy because it is heavy; it is heavy because of what you put in it.

This reframe matters because it changes what you do next. If you think the computer is dumb, the only move is to complain. If you accept that the instruction was ambiguous, you have a new job: find the ambiguous part and rewrite it. That second move is what an IT professional spends their day doing — sometimes in code, sometimes in tickets, sometimes in messages to other humans.

## Why this matters for an IT professional

In an IT job you write instructions all day, even when you are not writing code. You write tickets for colleagues. You write update notes for end users. You write search queries when you debug. You write small scripts that automate tasks. Every one of those is an instruction that someone — a human or a machine — will follow literally enough to get something wrong if you were not careful.

The skill of writing an instruction that cannot be misread is not glamorous, but it is the skill that separates a frustrated junior from a calm senior. Senior IT people do not write magic code; they write instructions that leave no room for guessing. The earlier you start practicing this, the cheaper it is. By the end of this course you will have practiced it in everyday language, in process descriptions, in pseudocode, and finally in JavaScript. The thinking is the same at every layer.

## Summary

This lesson set up the question the whole course is built around: *How do I speak to a computer so that it understands what I want it to do?* You saw that a computer reads instructions literally — like a sibling making a "sandwich" with the bread on the outside, or a search engine returning nothing useful for `pyhton tutorial`. You also saw the most important reframe of the lesson: when something goes wrong, the ambiguity is almost always in the instruction, not in the computer. That is good news, because instructions are something you can rewrite.

In the next lesson you will meet the word *algorithm*. An algorithm is just a clear sequence of literal steps that gets a job done — and you have already been writing them today without calling them that.
