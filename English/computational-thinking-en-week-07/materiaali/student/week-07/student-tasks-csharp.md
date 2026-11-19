# Week 7 — Student tasks (C#)

## Overview of this week's C# tasks

This week has **four tasks in the C# flavour**. The green-dot task (🟢 MANDATORY) is the **must-do minimum** — finish it to keep up with the class. The three purple-dot tasks (🟣 DEEPENING) are optional extensions; pick one or two if you have time.

Everything you write this week is the raw material for **AT3, which lands at the end of Week 8**. AT3 will ask you to translate a piece of your own Week-6 pseudocode into a tiny program in the language you pick this week. Save your code.

No IDE setup is required. No `dotnet new`, no Visual Studio, no .NET SDK install. C# runs this week inside a small online environment in the same browser you are reading this in. There is no testing framework this week; you run the code, you read the output, you compare it with what you predicted.

### How to open an online C# environment

- **Default — .NET Fiddle.** Go to `dotnetfiddle.net` in any browser. No account needed. Choose **Console** at the top. Paste your code lines inside the curly braces of `Main`, then press **Run**. The output appears in the lower box.
- **Alternative — sharplab.io.** Same idea, slightly different layout — also browser-based, no account.
- **Alternative — Replit (C#-enabled template).** Browser-based, optional sign-in.

Pick one and stick with it for the week.

---

## 🟢 MANDATORY — Your first console program (C#)

**Goal:** Run a first C# program in an online environment that prints a greeting, declares a variable, and does a small calculation. This is the must-do minimum of Week 7 in the C# path.

The screenshot you keep at the end of this task is exactly the kind of artefact AT3 will reuse next week.

### Steps

1. **Open .NET Fiddle** at `dotnetfiddle.net`. Choose **Console** at the top. You should see a small template with a `Main` method.
2. **Print a greeting with your real name.** Inside `Main`, type the line below using **your real name** in the quotes:

   ```csharp
   Console.WriteLine("Hello, <your name>");
   ```

   Press **Run**. If a red error appears, check the semicolon and the capitalisation in `Console.WriteLine`.
3. **Declare a variable for your age and print it.** Add two more lines, replacing `<your real age>` with the number for you:

   ```csharp
   int age = <your real age>;
   Console.WriteLine(age);
   ```

4. **Calculate years until adulthood and print it.** Two more lines:

   ```csharp
   int yearsToAdulthood = 18 - age;
   Console.WriteLine(yearsToAdulthood);
   ```

   If you are already 18 or older the number will be zero or negative — that is correct.
5. **Take a screenshot** of the output box showing all three lines in order. Paste it into your week-7 notes file.
6. **Write a 2–3 sentence reflection.** One thing that surprised you about C# (e.g. that you had to name the type `int` upfront); one thing that worked exactly as you predicted.

### Keep your notes

Keep the screenshot, the lines of code, and your reflection in one folder. **AT3 lands at the end of Week 8** and asks for a small program built on this exact shape — a variable, a calculation, an output. Re-using this code for AT3 is encouraged.

---

## 🟣 DEEPENING — First if/else (C#)

**Goal:** Write a 6-line C# program that uses an `if/else` to print one of two messages depending on a variable. The program from the L21 self-study, in your own hands.

### Steps

1. **In .NET Fiddle**, inside the `Main` method, paste the program below:

   ```csharp
   int age = 16;
   if (age >= 18)
   {
       Console.WriteLine("You may enter.");
   }
   else
   {
       Console.WriteLine("Sorry, you are not old enough.");
   }
   ```

2. **Predict before you run.** With `age = 16`, what do you expect the output box to print? Write it down **before** pressing **Run**.
3. **Run it.** Compare prediction with reality.
4. **Change the age to 19 and run again.** Predict again first. The output should switch branches.
5. **Screenshot both runs.** Save them next to your prediction notes.

### If you are doing this alone

This task does not assume a partner. If you want a second pair of eyes, use the **24-hour gap**: predict the output today, run the program tomorrow without re-reading your prediction.

### Keep your notes

Keep the program, both predictions, both screenshots. **AT3 lands at the end of Week 8** and asks for a small `if/else` program built on this exact shape. This task is the AT3 dress rehearsal.

---

## 🟣 DEEPENING — Translate your Week-6 pseudocode (C#)

**Goal:** Take one piece of your own Week-6 pseudocode that contains an `IF/ELSE` and turn it into a tiny C# program that runs in .NET Fiddle.

This is the most AT3-shaped task in the file. Doing it now means AT3 is half-written before it is released.

### Steps

1. **Pick one piece of Week-6 pseudocode** you wrote that has an `IF` (or `IF/ELSE`). The one you actually wrote yourself is best.
2. **Copy the pseudocode** into your notes file.
3. **Translate it into C#, line by line**:
   - `READ <something>` → `int <something> = <a value you choose>;` (or `string` if the value is text) for now.
   - `IF … THEN` → `if (…) {`.
   - `ELSE` → `} else {`.
   - `WRITE "…"` → `Console.WriteLine("…");`.
   - `ENDIF` → `}`.
4. **Paste the C# code into the `Main` method** and press **Run**. Read any red error message — the compiler usually points right at the line and tells you what word it did not like.
5. **Save pseudocode and C# side by side** in your notes. This is exactly the artefact AT3 will ask for.

### Keep your notes

Keep the pseudocode and the C#, side by side. **AT3 lands at the end of Week 8** and reuses this artefact directly.

---

## 🟣 DEEPENING — Break it on purpose (C#)

**Goal:** Deliberately introduce one mistake at a time into your working program from the first if/else task, and read the exact compiler message C# prints.

The point is to read **real** compiler messages so the first surprise error in AT3 does not stop you. C# is stricter than JavaScript here: many problems show up as a *compile* error before the program even tries to run, which is actually friendly.

### Steps

1. **Start from the working `if/else` program** from the *First if/else (C#)* task. Confirm it still runs cleanly.
2. **Break it three ways, one at a time**, and copy the exact compiler message:
   - **Forget a semicolon.** Remove the `;` at the end of the `int age = 16` line. (This is the classic C# compile error JavaScript would not have caught.)
   - **Mismatch a brace.** Delete the closing `}` of the `if` branch.
   - **Misspell the print function.** Change `Console.WriteLine` to `Console.WriteLin`.
3. **Fix each one** before introducing the next.
4. **Reflection (2–3 sentences):** which message was clearest? Which was confusing? Did any one point at the wrong line?

### If you are doing this alone

This task does not assume a partner — the compiler is your sparring partner. If you want a second opinion, post one error message in the class chat: *"Anyone else seen this one in C#?"*

### Keep your notes

Keep your three broken lines and the three exact compiler messages. **AT3 lands at the end of Week 8** and will involve at least one error message you have not seen before — a small library of C# errors written down now will speed you through that moment.
