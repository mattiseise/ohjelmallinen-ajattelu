# Lesson 21 — The age-limit check, three times

A walkthrough deck for L21. The same algorithm in pseudocode, then JavaScript, then C#. One transformation per slide.

---

## The Week-6 pseudocode we already know

```pseudo
READ age
IF age >= 18 THEN
  WRITE "You may enter."
ELSE
  WRITE "Sorry, you are not old enough."
ENDIF
```

A friend can follow this. A computer cannot — pseudocode is not in its word list.

---

## Step 1 — JavaScript, line by line

```javascript
let age = 16;
if (age >= 18) {
  console.log("You may enter.");
} else {
  console.log("Sorry, you are not old enough.");
}
```

`READ age` → `let age = 16;` (we hard-code for now).
`IF … THEN` → `if (…) {`.
`WRITE` → `console.log`.
`ENDIF` → `}`.

---

## Step 2 — C#, line by line

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

`READ age` → `int age = 16;`.
`IF … THEN` → `if (…) {`.
`WRITE` → `Console.WriteLine`.
`ENDIF` → `}`.

---

## What is the same in all three?

- The structure: *test, then-block, else-block*.
- The comparison `>=`.
- The two messages.
- The order of the lines, top to bottom.

The thinking does not change going from pseudocode to JS to C#.

---

## What is different?

- Real code needs an actual value: `let age = 16` or `int age = 16` instead of `READ age`.
- The print function: `console.log(...)` vs `Console.WriteLine(...)`.
- The type word in C# (`int`) — JavaScript figures the type out.
- Curly braces `{ }` replace `THEN … ELSE … ENDIF`.

These are the **syntax**. The differences are local. The thinking is shared.

---

## Predict — then run

Before clicking Run, predict the output for `age = 16`. Write it down. Then run.

```text
Sorry, you are not old enough.
```

Now change `age` to `19`. Predict again. Run again. The output should switch branches.

If both predictions matched reality, you have just dry-run code the same way you dry-ran pseudocode in Week 6.

---

## Hand-off to AT3

AT3 (Week 8) will ask you to take **one** piece of your own Week-6 pseudocode that has an `IF/ELSE` and turn it into a running program in JavaScript or C#.

The walkthrough on these slides is exactly the shape AT3 expects.

Save the code from today — it is the seed of next week's submission.
