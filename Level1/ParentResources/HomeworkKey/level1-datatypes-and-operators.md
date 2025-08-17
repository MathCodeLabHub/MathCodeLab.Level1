<img src="../../../CommonResources/Logo.MathCodeLab.Light.png#gh-light-mode-only" alt="MathCodeLab" width="150"/>
<img src="../../../CommonResources/Logo.MathCodeLab.Dark.jpg#gh-dark-mode-only" alt="MathCodeLab" width="150"/>

# Week 2 – Data Types, Variables, Operators & Blocks (Answer Key) ✅
These are the detailed solutions with reasoning for the Week 2 Advanced Homework.
Goal: move from “I can get the answer” → “I can explain the rule.”

Mentor tip: After each explanation, have the student invent a NEW similar example to prove understanding.

---
## Part A: Multiple Choice (1 pt each)
| Q | Answer | Explanation (Deep Dive) |
|---|--------|-------------------------|
| 1 | C (64) | `**` is exponent. `4 ** 3` = 4 × 4 × 4. Not 12 (that would be 4 + 8 mis-thinking) and not 81 (that’s 9 ** 2). |
| 2 | B (class) | `class` is a reserved keyword. Python blocks keyword use as identifiers so the parser isn’t confused. `my_var`, `total_3`, `varName` are valid. |
| 3 | A (18) | Order: parentheses → multiplication → floor division. (10 + 2)=12 → 12 * 3=36 → 36 // 2=18. Floor division here matches normal division because it divides evenly. |
| 4 | A (20) | Augmented assignments are sequential: start 7; `x += 3` → 10; `x *= 2` → 20. No precedence trick—just step-by-step updates. |
| 5 | C ("55") | String * int repeats the string. "5" * 2 → "55". Not numeric multiplication because left operand is text. |

Concept note: Repetition works only with an integer count: `"ha" * 3` → `"hahaha"`; `"ha" * 2.0` raises a `TypeError`.

---
## Part B: True / False (1 pt each)
| Q | Answer | Explanation (Why It Matters) |
|---|--------|-----------------------------|
| 6 | True | Dynamic typing: a name can later reference a different type (`x = 3` then `x = "three"`). Useful, but pick descriptive names to reduce confusion. |
| 7 | False | `"5" + 5` triggers a `TypeError` (runtime), not a syntax error (parse-time). Python refuses to guess the conversion. |
| 8 | True | `and` returns True only if BOTH operands are True; it short‑circuits (stops early) if the first is False. |
| 9 | True | Indentation = structure. It groups statements under headers (like `if`). Wrong indentation can change logic or break code. |
| 10 | False | `==` compares value equality; `is` tests identity (same object in memory). Two equal lists: `a == b` True, `a is b` False. |

Mini experiment:
```python
a = [1,2]
b = [1,2]
print(a == b)  # True (values equal)
print(a is b)  # False (different list objects)
```

---
## Part C: Short Answer & Fix the Bug (2 pts each)
**11)** `=` assignment (bind name to value). `==` equality comparison (returns True/False). Think: single '=' PUTS a value; double '==' CHECKS a value.

**12)** Error: `=>` is invalid. Use `>=`.
```python
if age >= 13:
    print("Teenager")
```
Explanation: Comparison operators must be exact (`>=`, `<=`, `==`, `!=`, `<`, `>`). `=>` is not one of them.

**13)** Output: `Even`
```python
num = 10
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```
Reason: `%` gives remainder. 10 % 2 = 0 → number divides evenly → even branch.

**14)** A block = indented group of lines under a colon-ended header (`if`, `for`, `while`, `def`, `class`). Indentation defines scope. Changing indentation changes which lines belong to the block. Python relies on this instead of curly braces.

**15)** Python 3 requires parentheses in `print` (it’s a function).
```python
name = "Sara"
print("Hello", name)
```
Extra note: Comma in print adds a space automatically; f-strings could also be used.

---
## Part D: Code Challenges (3 pts each)
**16) Two numbers: sum, difference, product, quotient**
```python
a = 12
b = 5
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)    # float division
```
Explanation: `/` is true division (returns float). Use `//` for floor division, `a % b` for remainder. Together `//` and `%` let you reconstruct: `(a // b) * b + (a % b) == a`.

**17) Positive / Negative / Zero**
```python
n = -3
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
```
Explanation: Mutually exclusive chain: first True condition “wins.” If `n` were 0 none of the first two are True so `else` handles it.

**18) Fruits + ratio (handle divide by zero)**
```python
apples = 6
oranges = 0
print("Total fruits:", apples + oranges)
if oranges != 0:
    print("Apple/Orange ratio:", apples / oranges)
else:
    print("Apple/Orange ratio: undefined (no oranges)")
```
Explanation: Guard condition prevents `ZeroDivisionError`. Alternative pattern: use a conditional expression in a single print.

**19) f-string formatting**
```python
name = "Sam"
score = 92
max_score = 100
print(f"Hello {name}, your score is {score} out of {max_score}.")
```
Explanation: f-strings evaluate expressions inside `{}`. Cleaner and faster than concatenation. Example enhancement: `f"{score/max_score:.0%}"` → `92%`.

**20) Voting eligibility**
```python
age_text = input("Enter age: ")
# Basic validation (optional):
# if not age_text.isdigit():
#     print("Enter digits only.")
# else:
age = int(age_text)
if age >= 18:
    print("You can vote.")
else:
    print("Not old enough yet.")
```
Explanation: `input()` returns a string. Cast to `int` for numeric comparison. Defensive coding adds validation.

---
## Part E: Code Tracing & Puzzles (3 pts each)
**21)**
```python
x = 3
y = 4
z = x + y * 2   # multiplication first: 4*2 = 8
print(z)         # 3 + 8 = 11
```
Output: `11`
Explanation: Operator precedence: `*` before `+`. Parentheses could override.

**22)**
```python
result = 10
result //= 3   # 10 // 3 = 3
result += 1    # now 4
print(result)
```
Output: `4`
Explanation: `//=` applies floor division then reassigns. Chaining steps mentally avoids mistakes.

**23) Fill in blanks**
Goal: Print whether `a` divisible by `b`.
```python
a = 7
b = 2
if a % b == 0:
    print("divisible")
else:
    print("not divisible")
```
Explanation: If remainder is 0 → divisible; any non-zero remainder means not divisible.

**24) Difference between / and //**
```python
a = 10
b = 3
print(a / b)   # 3.333333333... (float)
print(a // b)  # 3 (floor)
```
Explanation: `/` keeps the fractional part. `//` floors (toward negative infinity). For negatives: `-10 // 3` → `-4` (less than -3.33), not `-3`.

**25) Result is: 45**
We need `x * y + 5 = 45` → subtract 5 → `x * y = 40`.
Possible pairs: (5,8), (8,5), (10,4), (4,10), (20,2), (2,20), (40,1), (1,40).
```python
x = 5
y = 8
print("Result is:", x * y + 5)  # 45
```
Explanation: Solving simple linear expression by isolating the product. Core algebra skill.

---
## Quick Answer Summary
| Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|---|-----|
| 1 | 64  | 2 | class | 3 | 18 | 4 | 20 | 5 | "55" |
| 6 | T   | 7 | F | 8 | T | 9 | T | 10 | F |

Short answers quick recall: 11) assignment vs equality 12) >= 13) Even 14) Indented group 15) print(...)

---
### Further Practice Ideas
- Change numbers in Q16–Q20 and predict before running.
- Extend Q18: compute apple percentage: `apples / (apples + oranges)` when total > 0.
- Modify Q20: add branch for `age == 17` telling months until 18.
- Turn Q25 into: ask user for target total and constant add-on; solve `x * y + k = target`.

---
© 2025 MathCodeLab Team. All Rights Reserved.
