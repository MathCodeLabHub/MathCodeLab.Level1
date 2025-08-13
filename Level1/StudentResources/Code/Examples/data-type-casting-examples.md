<img src="../../../CommonResources/Logo.MathCodeLab.Light.png#gh-light-mode-only" alt="MathCodeLab" width="150"/>
<img src="../../../CommonResources/Logo.MathCodeLab.Dark.jpg#gh-dark-mode-only" alt="MathCodeLab" width="150"/>

# Data Type Casting – Practice Pack 🎒

Welcome, coder! These exercises help you practice changing data types in Python using `int()`, `float()`, and `str()`. Work top to bottom. Keep it simple—no functions needed.

---

## 🟢 Warm‑Ups (Try in order)

1) Number ➜ String
```python
age = 11
# Make a sentence like: I am 11 years old.
print("I am " + str(age) + " years old.")
```

2) String ➜ Number
```python
points_text = "25"
# Add 10 to points_text and print the total number
points = int(points_text)
print(points + 10)
```

3) Decimal ➜ Integer (Truncating)
```python
height = 4.98
# Turn height into a whole number and print it
print(int(height))
```

4) Number ➜ Decimal
```python
coins = 7
# Turn coins into a decimal number and print it
print(float(coins))
```

---

## 🧠 Predict the Output (then run to check!)

A)
```python
print(int(3.99))
```
Your guess: 3

B)
```python
price = "4.50"
print(float(price) + 1)
```
Your guess: 5.5

C)
```python
n = 12
print("Level " + str(n))
```
Your guess: Level 12

---

## 🛠️ Fix the Bug

1) What’s wrong? Make it run.
```python
score = "100"
print(int(score) + 20)
```

2) What’s wrong? Make it show: Total: 7.5
```python
x = "3.5"
y = 4
total = float(x) + y
print("Total:", total)
```

3) What will this print? Fix if needed.
```python
value = 5.6
print("Rounded:", round(value))    # Use round for normal rounding
```

---

## 🛒 Real‑World Mini Tasks

1) Shopping Cart Total
```python
prices_text = ["2.50", "1.25", "3.00"]
# Convert to numbers and print the total with 2 decimals
prices = [float(p) for p in prices_text]
print(f"Total: ${round(sum(prices), 2)}")
```

2) Quiz Average
```python
scores_text = ["9", "8", "10"]
# Convert to integers, print total and average
scores = [int(s) for s in scores_text]
print("Total:", sum(scores))
print("Average:", sum(scores) / len(scores))
```

3) Minutes ➜ Seconds
```python
minutes_text = "6"
# Turn into a number and print how many seconds
minutes = int(minutes_text)
print(minutes * 60)
```

4) Username Tag
```python
name = "Ava"
number = 42
# Print: Ava_42 (hint: mixing text + number)
print(name + "_" + str(number))
```

---

## 🎯 Challenge Corner

1) Clean Numbers
```python
# Turn these into integers safely and add them
data = ["10", " 20 ", "0030", "four"]
# Tip: use .strip() and .isdigit()
clean = []
for t in data:
    s = t.strip()
    if s.isdigit():
        clean.append(int(s))
print(sum(clean))
```

2) Nice Receipt
```python
# Given item prices (as text), print a receipt like:
# Item 1: $2.50
# Item 2: $1.00
# Total:  $3.50
items = ["2.50", "1.00"]
nums = [float(x) for x in items]
for i, price in enumerate(nums, start=1):
    print(f"Item {i}: ${price:.2f}")
print(f"Total:  ${sum(nums):.2f}")
```

3) Rounding Practice
```python
# Print these as:
# Raw: 3.678  | int: 3  | round: 4  | 1dp: 3.7
values = [3.678, 9.2, 5.5]
for v in values:
    print(f"Raw: {v}  | int: {int(v)}  | round: {round(v)}  | 1dp: {round(v, 1)}")
```

---

## 🧰 Helpful Hints
- `str(x)` ➜ make x into text
- `int(x)` ➜ whole number (fails if text isn’t number-like)
- `float(x)` ➜ decimal number
- `round(x, 2)` ➜ round to 2 decimal places
- Use f-strings to mix text and numbers: `f"Score: {score}"`
- `input()` always gives you a string!

---

## ✍️ Extra Credit (Optional)
- Ask the user for two numbers (as text) and print their sum.
- Ask for a price (like 4.5) and print the price with exactly 2 decimals.
- Ask for a whole number and show: int, float, and string versions.

---

© 2025 MathCodeLab Team. All Rights Reserved.
