# Week 7 — Student tasks (JavaScript)

## Overview of this week's JavaScript tasks

This week has **four tasks in the JavaScript flavour**. The green-dot task (🟢 MANDATORY) is the **must-do minimum** — finish it to keep up with the class. The three purple-dot tasks (🟣 DEEPENING) are optional extensions; pick one or two if you have time.

Everything you write this week is the raw material for **AT3, which lands at the end of Week 8**. AT3 will ask you to translate a piece of your own Week-6 pseudocode into a tiny program in the language you pick this week. Save your code.

No IDE setup is required. JavaScript runs in your browser's DevTools console. There is no testing framework this week; you run the code, you read the output, you compare it with what you predicted.

### How to open the JavaScript console

- **Mac**: `Cmd + Opt + J` in any browser.
- **Windows / Linux**: `Ctrl + Shift + J` in any browser.
- **Or**: right-click anywhere on the page, choose **Inspect**, then click the **Console** tab.

Paste a line, press Enter, read what appears.

---

## 🟢 MANDATORY — Your first console program (JS)

**Goal:** Run a first JavaScript program in your browser's console that prints a greeting, declares a variable, and does a small calculation. This is the must-do minimum of Week 7 in the JavaScript path.

The screenshot you keep at the end of this task is exactly the kind of artefact AT3 will reuse next week.

### Steps

1. **Open the console** in any browser (recipe above).
2. **Print a greeting with your real name.** Type the line below, using **your real name** in the quotes, then press Enter:

   ```javascript
   console.log("Hello, <your name>");
   ```

   If nothing appears, check the quotes and the dot in `console.log`.
3. **Declare a variable for your age and print it.** Replace `<your real age>` with the number for you:

   ```javascript
   let age = <your real age>;
   console.log(age);
   ```

4. **Calculate years until adulthood and print it.** Same console session:

   ```javascript
   let yearsToAdulthood = 18 - age;
   console.log(yearsToAdulthood);
   ```

   If you are already 18 or older, the number will be zero or negative — that is correct.
5. **Take a screenshot** of the console showing all three outputs in order. Paste it into your week-7 notes file.
6. **Write a 2–3 sentence reflection.** One thing that surprised you; one thing that worked exactly as you predicted.

### Keep your notes

Keep the screenshot, the three lines of code, and your reflection in one folder. **AT3 lands at the end of Week 8** and asks for a small program built on this exact shape — a variable, a calculation, an output. Re-using this code for AT3 is encouraged.

---

## 🟣 DEEPENING — First if/else (JS)

**Goal:** Write a 6-line JavaScript program that uses an `if/else` to print one of two messages depending on a variable. The program from the L21 self-study, in your own hands.

### Steps

1. **In the console**, paste the program below:

   ```javascript
   let age = 16;
   if (age >= 18) {
     console.log("You may enter.");
   } else {
     console.log("Sorry, you are not old enough.");
   }
   ```

2. **Predict before you run.** With `age = 16`, what do you expect the console to print? Write it down **before** pressing Enter.
3. **Run it.** Compare prediction with reality.
4. **Change the age to 19 and run again.** Predict again first. The output should switch branches.
5. **Screenshot both runs.** Save them next to your prediction notes.

### If you are doing this alone

This task does not assume a partner. If you want a second pair of eyes, use the **24-hour gap**: predict the output today, run the program tomorrow without re-reading your prediction.

### Keep your notes

Keep the program, both predictions, both screenshots. **AT3 lands at the end of Week 8** and asks for a small `if/else` program built on this exact shape. This task is the AT3 dress rehearsal.

---

## 🟣 DEEPENING — Translate your Week-6 pseudocode (JS)

**Goal:** Take one piece of your own Week-6 pseudocode that contains an `IF/ELSE` and turn it into a tiny JavaScript program that runs in the console.

This is the most AT3-shaped task in the file. Doing it now means AT3 is half-written before it is released.

### Steps

1. **Pick one piece of Week-6 pseudocode** you wrote that has an `IF` (or `IF/ELSE`). The one you actually wrote yourself is best.
2. **Copy the pseudocode** into your notes file.
3. **Translate it into JavaScript, line by line**:
   - `READ <something>` → `let <something> = <a value you choose>;` for now.
   - `IF … THEN` → `if (…) {`.
   - `ELSE` → `} else {`.
   - `WRITE "…"` → `console.log("…");`.
   - `ENDIF` → `}`.
4. **Paste the JavaScript into the console** and run it. Read any error message — the interpreter usually points right at the line.
5. **Save pseudocode and JavaScript side by side** in your notes. This is exactly the artefact AT3 will ask for.

### Keep your notes

Keep the pseudocode and the JS, side by side. **AT3 lands at the end of Week 8** and reuses this artefact directly.

---

## 🟣 DEEPENING — Break it on purpose (JS)

**Goal:** Deliberately introduce one mistake at a time into your working program from the first if/else task, and read the exact error message the JavaScript engine prints.

The point is to read **real** error messages so the first surprise error in AT3 does not stop you.

### Steps

1. **Start from the working `if/else` program** from the *First if/else (JS)* task. Confirm it still runs cleanly.
2. **Break it three ways, one at a time**, and copy the exact error message the console prints:
   - **Forget a quote.** Change `"You may enter."` to `"You may enter.` (no closing quote).
   - **Forget a closing brace.** Delete the last `}`.
   - **Misspell the print function.** Change `console.log` to `consle.log`.
3. **Fix each one** before introducing the next.
4. **Reflection (2–3 sentences):** which error message was clearest? Which was confusing? Did any one point at the wrong line?

### If you are doing this alone

This task does not assume a partner — the console is your sparring partner. If you want a second opinion, post one error message in the class chat: *"Anyone else seen this one in JS?"*

### Keep your notes

Keep your three broken lines and the three exact error messages. **AT3 lands at the end of Week 8** and will involve at least one error message you have not seen before — a small library of JS errors written down now will speed you through that moment.
