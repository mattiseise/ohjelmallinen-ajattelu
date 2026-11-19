# Decision trees — one tree, end to end

A supplementary deck for Lesson 14.

Walk one everyday decision tree slowly, then watch the same shape appear in an IT scene.

---

## The everyday rule

*"Should I take an umbrella today?"*

The rule, in one verbal sentence:

> If it is raining now, yes.
> If it is not raining but the forecast says rain, yes.
> Otherwise no.

---

## Draw the tree — branches and tests

```
            Is it raining now?
              /          \
            yes            no
            /                \
       take umbrella    Does the forecast
                          say rain?
                          /         \
                        yes          no
                        /              \
                  take umbrella   leave it at home
```

Root question at the top. Two tests, three leaves. Each test is something you can actually check.

---

## Express the rule as casual if … then …

- **if** *it is raining now*, **then** *take an umbrella*
- **else if** *the forecast says rain*, **then** *take an umbrella*
- **else** *leave it at home*

Same rule, written as English shorthand. Not code — just a layout that makes the test and the action easier to see.

---

## The IT mirror — should this login attempt be blocked?

The rule, in one verbal sentence:

> If the password is wrong and it is already the 4th try within 5 minutes, block the account.
> If the password is wrong but there have been fewer than 4 tries, ask the user to try again.
> If the password is right, log in.

---

## The same tree, different scene

```
              Is the password right?
                /              \
              yes                no
              /                    \
          log in           Has the user tried
                            4+ times in 5 min?
                              /          \
                            yes            no
                            /                \
                       block account     ask to retry
```

Three branches. Two tests. Same shape as the umbrella tree — different tests, different leaves.

---

## Naming the test honestly

The quality of a decision tree is the quality of the tests on its branches.

- Honest: *"Is it raining now?"*, *"Have they tried 4+ times in 5 minutes?"*
- Not honest yet: *"Will it rain at some point?"*, *"Is the user being suspicious?"*

If a test is vague, the follower has to guess — and the tree stops being useful.

Take-away: when you draw a tree this week, push every branch until the test is something a literal follower could check.
