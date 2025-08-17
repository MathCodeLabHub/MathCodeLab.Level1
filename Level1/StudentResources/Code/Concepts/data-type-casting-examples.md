<img src="../../../CommonResources/Logo.MathCodeLab.Light.png#gh-light-mode-only" alt="MathCodeLab" width="150"/>
<img src="../../../CommonResources/Logo.MathCodeLab.Dark.jpg#gh-dark-mode-only" alt="MathCodeLab" width="150"/>

# Data Type Casting in Python 🧙‍♂️

## What is Data Type Casting?
Data type casting is like changing the shape of a container so it can hold something different. In Python, it means **changing a value from one type to another** (like from a number to a string, or a string to a number).

---

## Why Do We Need Casting?
- Sometimes, you want to do math with numbers that are stored as text (strings).
- Or, you want to join a number with a sentence.
- Computers need to know exactly what kind of data they’re working with!

---

## How to Cast in Python (with Examples)

### 1. Changing a Number to a String
```python
age = 12
age_text = str(age)  # Now age_text is '12' (a string)
print("I am " + age_text + " years old.")
```

### 2. Changing a String to a Number
```python
score_text = "100"
score = int(score_text)  # Now score is 100 (an integer)
print(score + 50)  # Output: 150
```

### 3. Changing a Decimal to an Integer
```python
height = 1.75
height_whole = int(height)  # This will be 1 (it cuts off the decimal part)
print(height_whole)
```

### 4. Changing a Number to a Decimal
```python
points = 7
points_decimal = float(points)  # This will be 7.0
print(points_decimal)
```

---

## Real-World Examples You’ll See Often 🌍

### 1) Adding Scores from a Quiz (strings ➜ numbers)
```python
# Scores typed by students often come in as text
scores_text = ["8", "9", "10", "7"]

# Convert each to an integer and add them
scores = [int(s) for s in scores_text]

total = sum(scores)
average = total / len(scores)

print(f"Total: {total}")        # 34
print(f"Average: {average}")    # 8.5
```

### 2) Shopping Cart Total (strings ➜ decimals)
```python
# Prices read from a file or web form might be text
prices_text = ["3.50", "1.25", "2.00"]

# Convert to float to do money math
prices = [float(p) for p in prices_text]

total = sum(prices)
print(f"Your total is ${round(total, 2)}")  # Your total is $6.75
```

### 3) Timer App (minutes text ➜ seconds number)
```python
minutes_text = "3"        # user typed this
minutes = int(minutes_text)
seconds = minutes * 60
print(f"That is {seconds} seconds")  # That is 180 seconds
```

---

## Helpful Tricks 🧰

### Using f-strings (an easy way to mix text and numbers)
```python
age = 12
print(f"I am {age} years old.")  # No need for str(age)
```

### Rounding vs. Truncating
```python
value = 3.67
print(int(value))     # 3  (cuts off the decimal)
print(round(value))   # 4  (rounds to nearest whole number)
print(round(value, 1))# 3.7 (rounds to 1 decimal place)
```

### Reading Input (input() gives you text!)
```python
# input() always returns a string
text_number = input("Type a number: ")

# Simple safety check for digits only (good for basics)
if text_number.isdigit():
    n = int(text_number)
    print(f"Double is {n * 2}")
else:
    print("Please type only digits next time.")
```

### Quick Casts Cheat Sheet
- `str(x)` ➜ make x into text
- `int(x)` ➜ whole number (fails if x isn’t number-like text)
- `float(x)` ➜ decimal number
- `bool(x)` ➜ True/False (empty string `""` or `0` become False; most others become True)

---

## Relevance in Computer Science & Math
- **Computer Science:**
  - Data from users or files is often text. You need to cast it to numbers to do calculations!
  - When saving or sending data, you might need to turn numbers into strings.
- **Mathematics:**
  - Sometimes you want to do math with whole numbers (integers), and sometimes with decimals (floats).
  - Casting helps you control how precise your answers are.

---

## Common Mistakes
- Trying to cast a word (like "hello") to a number will cause an error!
- Casting a decimal to an integer **removes** the decimal part (it doesn’t round).

---

## Try It Yourself!
1. Turn your age (as a number) into a string and print a sentence with it.
2. Add two numbers that are stored as strings (hint: cast them to integers first!).
3. Try casting a decimal to an integer and see what happens.

---

© 2025 MathCodeLab Team. All Rights Reserved.
