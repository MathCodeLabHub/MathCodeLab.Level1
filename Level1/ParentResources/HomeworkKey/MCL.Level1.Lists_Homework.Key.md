<div style="text-align: center;">
  <img src="../../../../../CommonResources/Logo.MathCodeLab.Dark.jpg" alt="MathCodeLab Logo" style="max-width: 300px; margin-bottom: 20px;">
</div>

# 🔑 Answer Key: Lists Homework (SingleNumericLists_Homework.pdf)

**Course:** Level 1 - Lists  
**Document:** Lists_Homework.pdf / SingleNumericLists_Homework.pdf  
**For:** Instructors and Parents

---

## 📋 Table of Contents
- [Core Problems (1-15)](#core-problems)
- [Bonus Challenges](#bonus-challenges)
- [Testing Notes](#testing-notes)
- [Common Student Errors](#common-student-errors)

---

## 🔢 Core Problems

### 1️⃣ Sum of Numbers in a List

**Problem:** Find the sum without using `sum()`.

**Solution:**
```python
numbers = [10, 20, 30, 40, 50]

total = 0
for num in numbers:
    total = total + num

print("Sum:", total)
```

**Output:** `Sum: 150`

**Step-by-Step:**
```
Start: total = 0
Add 10: total = 0 + 10 = 10
Add 20: total = 10 + 20 = 30
Add 30: total = 30 + 30 = 60
Add 40: total = 60 + 40 = 100
Add 50: total = 100 + 50 = 150
```

**Key Concept:** Accumulator pattern - start at 0, add each element

---

### 2️⃣ Minimum Number in a List

**Problem:** Find smallest number without using `min()`.

**Solution:**
```python
numbers = [45, 12, 78, 23, 9, 56]

# Start with first number as minimum
minimum = numbers[0]

# Check each number
for num in numbers:
    if num < minimum:
        minimum = num

print("Minimum:", minimum)
```

**Output:** `Minimum: 9`

**Algorithm Trace:**
```
Start: minimum = 45
Check 45: 45 < 45? No
Check 12: 12 < 45? Yes → minimum = 12
Check 78: 78 < 12? No
Check 23: 23 < 12? No
Check 9:  9 < 12? Yes → minimum = 9
Check 56: 56 < 9? No
Result: 9
```

**Key Concept:** Comparison pattern - assume first is smallest, update when finding smaller

---

### 3️⃣ Maximum Number in a List

**Problem:** Find largest number without using `max()`.

**Solution:**
```python
numbers = [45, 12, 78, 23, 9, 56]

# Start with first number as maximum
maximum = numbers[0]

# Check each number
for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum:", maximum)
```

**Output:** `Maximum: 78`

**Algorithm Trace:**
```
Start: maximum = 45
Check 45: 45 > 45? No
Check 12: 12 > 45? No
Check 78: 78 > 45? Yes → maximum = 78
Check 23: 23 > 78? No
Check 9:  9 > 78? No
Check 56: 56 > 78? No
Result: 78
```

**Key Concept:** Same as minimum, but with > instead of <

---

### 4️⃣ Count Even and Odd Numbers

**Problem:** Count even and odd numbers separately.

**Solution:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("Even:", even_count)
print("Odd:", odd_count)
```

**Output:**
```
Even: 5
Odd: 5
```

**Explanation:**
- `%` (modulo) gives remainder when dividing
- Even numbers: remainder is 0 when divided by 2
- Odd numbers: remainder is 1 when divided by 2

**Even numbers:** 2, 4, 6, 8, 10 = 5 numbers  
**Odd numbers:** 1, 3, 5, 7, 9 = 5 numbers

---

### 5️⃣ Count Positive and Negative Numbers

**Problem:** Count positive, negative, and zero values.

**Solution:**
```python
numbers = [10, -5, 20, -15, 0, 30, -8]

positive_count = 0
negative_count = 0
zero_count = 0

for num in numbers:
    if num > 0:
        positive_count = positive_count + 1
    elif num < 0:
        negative_count = negative_count + 1
    else:
        zero_count = zero_count + 1

print("Positive:", positive_count)
print("Negative:", negative_count)
print("Zero:", zero_count)
```

**Output:**
```
Positive: 3
Negative: 3
Zero: 1
```

**Breakdown:**
- Positive: 10, 20, 30 = 3
- Negative: -5, -15, -8 = 3
- Zero: 0 = 1

---

### 6️⃣ Find the Average of List Elements

**Problem:** Calculate average without `sum()` or `len()`.

**Solution:**
```python
numbers = [10, 20, 30, 40, 50]

# Calculate sum
total = 0
for num in numbers:
    total = total + num

# Count elements
count = 0
for num in numbers:
    count = count + 1

# Calculate average
average = total / count

print("Average:", average)
```

**More Efficient (One Loop):**
```python
numbers = [10, 20, 30, 40, 50]

total = 0
count = 0

for num in numbers:
    total = total + num
    count = count + 1

average = total / count
print("Average:", average)
```

**Output:** `Average: 30.0`

**Calculation:**
- Sum: 10 + 20 + 30 + 40 + 50 = 150
- Count: 5
- Average: 150 ÷ 5 = 30.0

---

### 7️⃣ Find Second Largest Number

**Problem:** Find second largest without sorting.

**Solution:**
```python
numbers = [45, 12, 78, 23, 56, 89]

# Initialize both with first element
largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        # New largest found
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        # New second largest found
        second_largest = num

print("Second largest:", second_largest)
```

**Output:** `Second largest: 78`

**Algorithm Trace:**
```
Start: largest = 45, second_largest = 45

Check 45: Skip (same as start)
Check 12: 12 > 45? No
Check 78: 78 > 45? Yes → second_largest = 45, largest = 78
Check 23: 23 > 45? No
Check 56: 56 > 78? No, 56 > 45? Yes → second_largest = 56
Check 89: 89 > 78? Yes → second_largest = 78, largest = 89

Result: largest = 89, second_largest = 78
```

---

### 8️⃣ Reverse a List

**Problem:** Reverse without using `reverse()` or slicing.

**Solution Method 1 (Using Negative Indexes):**
```python
numbers = [1, 2, 3, 4, 5]

reversed_list = []

# Count elements
length = 0
for num in numbers:
    length = length + 1

# Add from end to beginning
for i in range(1, length + 1):
    reversed_list.append(numbers[-i])

print("Reversed:", reversed_list)
```

**Solution Method 2 (Using Range Backwards):**
```python
numbers = [1, 2, 3, 4, 5]

reversed_list = []

# Count elements
length = 0
for num in numbers:
    length = length + 1

# Loop backwards through indexes
for i in range(length - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Reversed:", reversed_list)
```

**Output:** `Reversed: [5, 4, 3, 2, 1]`

**How Method 1 Works:**
```
numbers[-1] = 5 → append to reversed_list
numbers[-2] = 4 → append to reversed_list
numbers[-3] = 3 → append to reversed_list
numbers[-4] = 2 → append to reversed_list
numbers[-5] = 1 → append to reversed_list
Result: [5, 4, 3, 2, 1]
```

---

### 9️⃣ Find the Product of All Numbers

**Problem:** Multiply all numbers together.

**Solution:**
```python
numbers = [2, 3, 4, 5]

# IMPORTANT: Start with 1, not 0!
product = 1

for num in numbers:
    product = product * num

print("Product:", product)
```

**Output:** `Product: 120`

**Step-by-Step:**
```
Start: product = 1
Multiply by 2: product = 1 × 2 = 2
Multiply by 3: product = 2 × 3 = 6
Multiply by 4: product = 6 × 4 = 24
Multiply by 5: product = 24 × 5 = 120
```

**⚠️ Common Error:** Starting with `product = 0` makes everything 0!

---

### 🔟 Find Difference Between Largest and Smallest

**Problem:** Find the range (max - min) without using built-in functions.

**Solution:**
```python
numbers = [45, 12, 78, 23, 9, 56]

# Find minimum
minimum = numbers[0]
for num in numbers:
    if num < minimum:
        minimum = num

# Find maximum
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num

# Calculate difference
difference = maximum - minimum

print("Largest:", maximum)
print("Smallest:", minimum)
print("Difference:", difference)
```

**More Efficient (One Loop):**
```python
numbers = [45, 12, 78, 23, 9, 56]

minimum = numbers[0]
maximum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

difference = maximum - minimum

print("Difference:", difference)
```

**Output:** `Difference: 69`

**Calculation:** 78 - 9 = 69

---

### 1️⃣1️⃣ Find All Numbers Greater Than a Given Value

**Problem:** Filter numbers greater than threshold.

**Solution:**
```python
numbers = [10, 25, 30, 15, 40, 5]
x = 20

greater_than_x = []

for num in numbers:
    if num > x:
        greater_than_x.append(num)

print("Numbers greater than", x, ":", greater_than_x)
```

**Output:** `Numbers greater than 20 : [25, 30, 40]`

**Visual Filter:**
```
[10, 25, 30, 15, 40, 5]
 ✗   ✓   ✓   ✗   ✓  ✗   (comparing with 20)
     ↓   ↓       ↓
    [25, 30,    40]
```

---

### 1️⃣2️⃣ Check if a Number Exists in the List

**Problem:** Search without using `in` keyword.

**Solution:**
```python
numbers = [10, 25, 30, 15, 40]
search = 30

# Use flag to track if found
found = False

for num in numbers:
    if num == search:
        found = True
        break  # Can stop once found (optional optimization)

if found:
    print(search, "exists in the list")
else:
    print(search, "does not exist in the list")
```

**Output:** `30 exists in the list`

**Key Concept:** Flag pattern - use boolean variable to remember result

---

### 1️⃣3️⃣ Count Occurrences of a Number

**Problem:** Count appearances without `.count()`.

**Solution:**
```python
numbers = [5, 10, 5, 20, 5, 30]
search = 5

count = 0

for num in numbers:
    if num == search:
        count = count + 1

print(search, "appears", count, "times")
```

**Output:** `5 appears 3 times`

**Trace:**
```
Check 5: 5 == 5? Yes → count = 1
Check 10: 10 == 5? No
Check 5: 5 == 5? Yes → count = 2
Check 20: 20 == 5? No
Check 5: 5 == 5? Yes → count = 3
Check 30: 30 == 5? No
Result: 3
```

---

### 1️⃣4️⃣ Find Both Smallest and Largest in One Loop

**Problem:** Find min and max with single loop.

**Solution:**
```python
numbers = [45, 12, 78, 23, 9, 56]

# Initialize both with first element
smallest = numbers[0]
largest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print("Smallest:", smallest)
print("Largest:", largest)
```

**Output:**
```
Smallest: 9
Largest: 78
```

**Why This Works:**
- We check both conditions in the same loop
- More efficient than two separate loops
- Both comparisons are independent

---

### 1️⃣5️⃣ Swap First and Last Elements

**Problem:** Exchange first and last values.

**Solution Method 1 (Using Temporary Variable):**
```python
numbers = [10, 20, 30, 40, 50]

# Save first element
temp = numbers[0]

# Move last to first
numbers[0] = numbers[-1]

# Move saved first to last
numbers[-1] = temp

print("After swap:", numbers)
```

**Solution Method 2 (Using Tuple Unpacking):**
```python
numbers = [10, 20, 30, 40, 50]

# Python's elegant way to swap
numbers[0], numbers[-1] = numbers[-1], numbers[0]

print("After swap:", numbers)
```

**Output:** `After swap: [50, 20, 30, 40, 10]`

**Visual:**
```
Before: [10, 20, 30, 40, 50]
         ↓               ↓
         ↓←──────────────↓
         
After:  [50, 20, 30, 40, 10]
```

---

## 🌟 Bonus Challenges

### 🎁 Bonus 1: Remove Duplicates

**Problem:** Remove duplicates without using `set()`.

**Solution:**
```python
numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = []

for num in numbers:
    # Check if already in unique list
    already_exists = False
    
    for unique_num in unique_numbers:
        if num == unique_num:
            already_exists = True
            break
    
    # Add only if not already there
    if not already_exists:
        unique_numbers.append(num)

print("Unique numbers:", unique_numbers)
```

**Output:** `Unique numbers: [1, 2, 3, 4, 5]`

**How It Works:**
```
Check 1: Not in unique_numbers → add [1]
Check 2: Not in unique_numbers → add [1, 2]
Check 2: Already in list → skip
Check 3: Not in unique_numbers → add [1, 2, 3]
Check 4: Not in unique_numbers → add [1, 2, 3, 4]
Check 4: Already in list → skip
Check 5: Not in unique_numbers → add [1, 2, 3, 4, 5]
```

---

### 🎁 Bonus 2: Find Common Elements Between Two Lists

**Problem:** Find elements appearing in both lists.

**Solution:**
```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common = []

# Check each element in list1
for num1 in list1:
    # See if it exists in list2
    for num2 in list2:
        if num1 == num2:
            # Found a match, check if not already added
            already_added = False
            for item in common:
                if item == num1:
                    already_added = True
                    break
            
            if not already_added:
                common.append(num1)
            break  # Found it, no need to continue inner loop

print("Common elements:", common)
```

**Simpler Solution:**
```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common = []

for num1 in list1:
    # Check if num1 is in list2
    found_in_list2 = False
    for num2 in list2:
        if num1 == num2:
            found_in_list2 = True
            break
    
    # If found in list2, add to common
    if found_in_list2:
        common.append(num1)

print("Common elements:", common)
```

**Output:** `Common elements: [4, 5]`

**Visual:**
```
list1: [1, 2, 3, 4, 5]
list2: [4, 5, 6, 7, 8]
             ↓  ↓
Common:     [4, 5]
```

---

### 🎁 Bonus 3: Rotate List by N Positions

**Problem:** Rotate list to the right by n positions.

**Solution:**
```python
numbers = [1, 2, 3, 4, 5]
n = 2

# Find length
length = 0
for num in numbers:
    length = length + 1

# Create rotated list
rotated = []

# Start from position (length - n) and wrap around
for i in range(length):
    # Calculate new position
    new_index = (length - n + i) % length
    rotated.append(numbers[new_index])

print("Original:", numbers)
print("Rotated by", n, ":", rotated)
```

**Alternative (Simpler Approach):**
```python
numbers = [1, 2, 3, 4, 5]
n = 2

# Find length
length = 0
for num in numbers:
    length = length + 1

# Split into two parts and recombine
# Take last n elements
last_part = []
for i in range(length - n, length):
    last_part.append(numbers[i])

# Take first (length - n) elements
first_part = []
for i in range(0, length - n):
    first_part.append(numbers[i])

# Combine
rotated = last_part + first_part

print("Rotated:", rotated)
```

**Output:** `Rotated: [4, 5, 1, 2, 3]`

**Visual:**
```
Original:  [1, 2, 3, 4, 5]
             ↓  ↓  ↓  ↓  ↓
Rotate by 2: Move last 2 to front
             [4, 5] → front
             [1, 2, 3] → after

Result:    [4, 5, 1, 2, 3]
```

---

## 📊 Testing Notes

### Test Cases for Each Problem

**For Sum, Average, Product:**
- Normal: `[10, 20, 30]`
- Single element: `[5]`
- Negative numbers: `[-5, -10, 15]`
- With zero: `[0, 5, 10]`

**For Min/Max:**
- Normal: `[45, 12, 78, 23]`
- All same: `[5, 5, 5]`
- Negative numbers: `[-10, -5, -20]`
- Mixed: `[-5, 0, 10, -3]`

**For Even/Odd Counting:**
- All even: `[2, 4, 6, 8]`
- All odd: `[1, 3, 5, 7]`
- Mixed: `[1, 2, 3, 4, 5]`
- With zero: `[0, 1, 2]` (zero is even!)

**Edge Cases:**
- Empty list: `[]` (will cause errors in current solutions)
- Single element: `[5]`
- Two elements: `[3, 7]`

---

## ⚠️ Common Student Errors

### Error 1: Wrong Initialization for Product
```python
# ❌ WRONG
product = 0  # This makes everything 0!

# ✅ CORRECT
product = 1  # Start with 1 for multiplication
```

### Error 2: Not Initializing Variables
```python
# ❌ WRONG
for num in numbers:
    total = total + num  # total is not defined!

# ✅ CORRECT
total = 0  # Initialize first
for num in numbers:
    total = total + num
```

### Error 3: Modifying List While Iterating
```python
# ❌ WRONG (can cause problems)
for num in numbers:
    if num < 0:
        numbers.remove(num)

# ✅ CORRECT (create new list)
positive_numbers = []
for num in numbers:
    if num >= 0:
        positive_numbers.append(num)
```

### Error 4: Off-by-One in Range
```python
# ❌ WRONG
for i in range(1, length):  # Misses first or last element

# ✅ CORRECT
for i in range(length):  # Gets all elements (0 to length-1)
```

### Error 5: Forgetting to Handle Zero
```python
# ❌ INCOMPLETE
if num > 0:
    positive_count += 1
else:
    negative_count += 1  # This counts zero as negative!

# ✅ CORRECT
if num > 0:
    positive_count += 1
elif num < 0:
    negative_count += 1
else:
    zero_count += 1
```

---

## 🎓 Grading Rubric

### Points Breakdown (per problem):
- **Correctness (40%)**: Does it produce the right output?
- **Logic (30%)**: Is the algorithm correct?
- **Code Quality (20%)**: Is it readable and well-structured?
- **Comments (10%)**: Are there helpful explanations?

### Deductions:
- Using forbidden functions (like `sum()`, `max()`): -100% for that problem
- Syntax errors: -20%
- Logic errors: -40%
- Missing edge case handling: -10%
- No comments: -10%

---

## 💡 Teaching Tips

1. **Start with Tracing:** Walk through each problem step-by-step on paper first
2. **Use Visual Aids:** Draw the list and show how variables change
3. **Test Incrementally:** Have students test after each problem
4. **Encourage Debugging:** Teach using print statements to debug
5. **Discuss Efficiency:** Compare one-loop vs. two-loop solutions
6. **Connect Concepts:** Show how patterns repeat across problems

---

<div style="text-align: center; margin-top: 40px; padding: 20px; border-top: 2px solid #ccc;">
  <p><strong>MathCodeLab</strong> | Empowering Young Minds Through Code</p>
  <p>© 2025 MathCodeLab Team. All Rights Reserved.</p>
  <p><em>🔒 This Answer Key is for Instructors and Parents Only</em></p>
</div>
