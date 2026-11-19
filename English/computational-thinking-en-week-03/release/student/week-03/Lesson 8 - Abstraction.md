# Lesson 8 — Abstraction

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
