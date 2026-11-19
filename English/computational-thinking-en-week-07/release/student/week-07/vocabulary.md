# Vocabulary

## Week 7 vocabulary

The terms below cover Lessons 19, 20 and 21. Definitions are short on purpose — read the self-study for examples in context. Two terms (`console.log` and `Console.WriteLine`) are language-specific entries paired side by side. One term at the end (*loop*) is a preview of Week 8, flagged as such.

### Programming language

A set of words and rules a computer can read and run. JavaScript and C# are two such languages. A programming language differs from pseudocode in that the computer itself can interpret or compile it, not just a human reader. The thinking — sequence, condition, repetition — is the same as in pseudocode; the language is just the precise shape it takes.

### Syntax

The rule for *how words have to be arranged* in a programming language. Which words exist, in what order they may appear, what punctuation has to surround them, where a statement ends. Code that follows the syntax runs. Code that breaks the syntax stops with an error message. Syntax is what the computer reads; the thinking is what you write.

### Command

A single instruction the computer can carry out. `console.log("Hello")` is a command: "print the text *Hello* to the console." `int age = 16;` is a command: "make a variable called `age`, of type `int`, and put `16` in it." Programs are sequences of commands, one after another.

### Interpreter *(informal)*

A program that reads your code one line at a time and runs each line as it goes. JavaScript in the browser is interpreted: paste a line into the console, press Enter, see the result. There is no separate "build then run" step.

### Compiler *(informal)*

A program that reads your whole code at once, translates it into a lower-level form the computer can run faster, and then runs that translated version. C# is compiled before it runs. From a student's point of view this week, the main difference is that a compiler can refuse to even start if your code has a syntax error.

### Console

A small text area where a program prints output and (sometimes) reads input. The browser **DevTools console** is the place JavaScript prints to. **.NET Fiddle's** output box is the place C# prints to. The console is where Week-6 pseudocode's `WRITE` finally lands — on a real screen, in a real program.

### Output

What a program sends out to be seen — a line of text in the console, a number, a yes/no. In JavaScript, you write output with `console.log(...)`. In C#, with `Console.WriteLine(...)`. Output is how a program talks back.

### Variable

A named container for one value that can change while the program runs. *(Same idea as Week 6, now in a real language.)* In JavaScript: `let age = 16;`. In C#: `int age = 16;`. The label `age` stays the same; the value inside can change. A good variable name describes what the value means.

### Value

The actual content stored in a variable at a given moment — a piece of text (`"Lyra"`), a whole number (`16`), a yes/no (`true`). The variable is the labelled box; the value is what is inside the box right now.

### Assignment

The action of putting a value into a variable. Both JavaScript and C# write it with `=`. `let age = 16;` (JS) and `int age = 16;` (C#) are assignments. The pseudocode `SET age TO 16` is the same idea in a different surface.

### String

A piece of text, written between quotes. `"Hello, console"` is a string. `"16"` is also a string, even though it looks like a number — the quotes make it text. Both JavaScript and C# use double quotes. The word *string* is short for "string of characters."

### Int / number

A whole number, used in code as a value with no quotes around it. C# calls this type **`int`** (short for *integer*) and asks you to name it when you declare the variable: `int age = 16;`. JavaScript just calls it a **number** and figures it out from the value: `let age = 16;`. `16` is an int / number; `"16"` is a string.

### Condition

A small expression that is either true or false, written inside the round brackets of an `if`. `age >= 18` is a condition. The whole point of a condition is that an `if/else` can take a different branch depending on whether the condition is true. *(Revisited from Week 6 — same idea, now in code.)*

### If / else

A control structure that runs one block of code if a condition is true, and another block if it is false. In both JavaScript and C#: `if (test) { ... } else { ... }`. The `else` part is optional — `if` alone is valid code. *(Revisited from Week 6 — same idea, now in code.)*

### Comparison operator

A symbol that compares two values and produces a true / false result. The six this course uses are `==` (equal), `!=` (not equal), `>` (greater than), `>=` (greater than or equal), `<` (less than), `<=` (less than or equal). These six are essentially identical in JavaScript and C#. (JavaScript also has `===`, which is a stricter form of equality; either form works for what we do this week.)

### `console.log` *(JavaScript)*

The JavaScript command that prints to the console. `console.log("Hello")` prints `Hello` on its own line. You can pass it a string, a number, a variable, or several values separated by commas. It is the main way a JavaScript program shows you what is happening.

### `Console.WriteLine` *(C#)*

The C# command that prints to the console. `Console.WriteLine("Hello");` prints `Hello` on its own line, followed by a line break. The `WriteLine` part is one word, the capital `W` and capital `L` matter. The semicolon at the end is mandatory in C#.

### Loop *(looking ahead — central topic of Week 8)*

A control structure that runs a block of code several times in a row, with a stopping condition. You met the idea in Week-6 pseudocode as `WHILE` and `FOR`. Next week the same idea arrives in JavaScript and C# as `while` and `for`, side by side. You do not need to write loops in code this week — the term is here so the word is not new in Week 8.
