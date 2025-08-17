<img src="../../../CommonResources/Logo.MathCodeLab.Light.png#gh-light-mode-only" alt="MathCodeLab" width="150"/>
<img src="../../../CommonResources/Logo.MathCodeLab.Dark.jpg#gh-dark-mode-only" alt="MathCodeLab" width="150"/>

# MCL.Level1.Loops – Solutions & Explanations 🧠🐍

Short, clear solutions for four classic beginner problems. Read the explanation, then study the code. No functions needed.

---
## 1) Numbers 1–50 Divisible by BOTH 3 and 5
We want numbers that are multiples of 3 AND 5 at the same time. A number divisible by both 3 and 5 is divisible by 15 (Least Common Multiple). So we can just check `n % 15 == 0` (or use `n % 3 == 0 and n % 5 == 0`).

### Code
```python
# Print numbers from 1 to 50 divisible by BOTH 3 and 5
for n in range(1, 51):
    if n % 15 == 0:    # could also do: if n % 3 == 0 and n % 5 == 0:
        print(n)
```
### Output
15, 30, 45 (each on its own line)

---
## 2) Multiplication Table for a Given Number
We store (or read) a number, then loop from 1 to 10 and multiply. We use an f-string so the format looks like: `7 x 3 = 21`.

### Code (fixed number example)
```python
num = 7        # change this number or replace with input if you like
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```
### (Optional) With user input
```python
num_text = input("Enter a number: ")
num = int(num_text)
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

---
## 3) Collatz‑Style Sequence (Sometimes Called 3n + 1)
Rule:
- Start with `n`.
- If the number is even → divide by 2.
- If the number is odd → multiply by 3 and add 1.
- Keep going until you reach 1.
The examples given match this pattern:
- 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
- 15 → 46 → 23 → 70 → … → 1

We append each value to a list so we can print the full sequence at the end.

### Code
```python
n_text = input("Enter a starting number: ")
n = int(n_text)
sequence = []

while n != 1:
    sequence.append(n)
    if n % 2 == 0:      # even
        n = n // 2
    else:               # odd
        n = 3 * n + 1

sequence.append(1)  # final 1
print(", ".join(str(x) for x in sequence))
```
### Explanation
We keep transforming the number. Even numbers shrink fast. Odd numbers jump up (3n+1) but eventually the value falls back down through divisions by 2. This famous sequence is unproven for ALL starting numbers, but it works for every number ever checked by computers.

---
## 4) Caterpillar Climb (Reach the Top Day Count)
Story:
- Height of pole: H (example 10)
- Climbs up A each day (example 3)
- Slips down B each night (example 2)
- On the FINAL day it does NOT slip back.

Key idea: Each full day (except the last) gains `(A - B)` feet. We simulate day by day until height ≥ H right AFTER a climb.

### Code (with sample values)
```python
H = 10  # pole height
A = 3   # climbs during the day
B = 2   # slips at night

height = 0
days = 0

while True:
    days += 1
    height += A          # daytime climb
    if height >= H:      # reached or passed the top -> stop (no slip)
        break
    height -= B          # night slip

print(f"Days needed: {days}")
```
### Faster Math (Optional Thinking)
If you wanted a formula: After (d - 1) full days, height gained is `(d - 1) * (A - B)`. On day d you add `A` and must reach ≥ H.
So: `(d - 1) * (A - B) + A ≥ H` → Solve for d. But for beginners, simulation is clearer and avoids mistakes.

---
### Summary Table
| Problem | Core Idea | Tool Used |
|---------|-----------|-----------|
| 1 | Divisible by both 3 & 5 → use % 15 | Modulo + loop |
| 2 | Repeat multiply 1..10 | for loop + f-string |
| 3 | Collatz rules until 1 | while loop + even/odd test |
| 4 | Gain A, lose B (except final) | while loop + break |

---
© 2025 MathCodeLab Team. All Rights Reserved.
