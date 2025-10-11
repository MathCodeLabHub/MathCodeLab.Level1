<div style="text-align: center;">
  <img src="../../../../CommonResources/Logo.MathCodeLab.Dark.jpg" alt="MathCodeLab Logo" style="max-width: 300px; margin-bottom: 20px;">
</div>

# 🔑 Homework Answer Key: Lists

## 📋 Table of Contents
1. [Basic List Operations](#basic-list-operations)
2. [Finding Min/Max](#finding-minmax)
3. [Counting and Filtering](#counting-and-filtering)
4. [List Transformations](#list-transformations)
5. [String Lists](#string-lists)
6. [Advanced Problems](#advanced-problems)

---

## 🔢 Basic List Operations

### Problem 1: Sum of Numbers
**Question:** Find the sum of all numbers in a list without using `sum()`.

**Solution:**
```python
numbers = [10, 20, 30, 40, 50]

total = 0
for num in numbers:
    total = total + num

print("Sum:", total)
```

**Output:** `Sum: 150`

**Explanation:**
- Start with `total = 0`
- Add each number one by one
- 0 + 10 = 10, 10 + 20 = 30, 30 + 30 = 60, 60 + 40 = 100, 100 + 50 = 150

---

### Problem 2: Find Average
**Question:** Calculate the average without using `sum()` or `len()`.

**Solution:**
```python
scores = [85, 92, 78, 95, 88]

# Calculate sum
total = 0
for score in scores:
    total = total + score

# Count items
count = 0
for score in scores:
    count = count + 1

# Calculate average
average = total / count

print("Average:", average)
```

**Output:** `Average: 87.6`

**Explanation:**
- First, add all numbers: 85 + 92 + 78 + 95 + 88 = 438
- Then, count items: 5
- Finally, divide: 438 ÷ 5 = 87.6

---

### Problem 3: Product of All Numbers
**Question:** Find the product of all numbers (multiply them).

**Solution:**
```python
numbers = [2, 3, 4, 5]

product = 1  # Start with 1, not 0!
for num in numbers:
    product = product * num

print("Product:", product)
```

**Output:** `Product: 120`

**Explanation:**
- Start with `product = 1` (if you start with 0, everything becomes 0!)
- Multiply each number: 1 × 2 = 2, 2 × 3 = 6, 6 × 4 = 24, 24 × 5 = 120

---

### Problem 4: Count Items in List
**Question:** Count how many items are in a list without using `len()`.

**Solution:**
```python
fruits = ["apple", "banana", "cherry", "date"]

count = 0
for fruit in fruits:
    count = count + 1

print("Total items:", count)
```

**Output:** `Total items: 4`

**Explanation:**
- Start with `count = 0`
- Add 1 for each item in the list

---

## 🔍 Finding Min/Max

### Problem 5: Find Minimum
**Question:** Find the smallest number without using `min()`.

**Solution:**
```python
numbers = [45, 12, 78, 23, 9, 56]

minimum = numbers[0]  # Start with first number

for num in numbers:
    if num < minimum:
        minimum = num

print("Minimum:", minimum)
```

**Output:** `Minimum: 9`

**Explanation:**
- Assume first number (45) is smallest
- Compare each number and update if smaller
- 12 < 45, so minimum = 12
- 9 < 12, so minimum = 9 (final answer)

---

### Problem 6: Find Maximum
**Question:** Find the largest number without using `max()`.

**Solution:**
```python
numbers = [45, 12, 78, 23, 9, 56]

maximum = numbers[0]  # Start with first number

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum:", maximum)
```

**Output:** `Maximum: 78`

**Explanation:**
- Assume first number (45) is largest
- Compare each number and update if larger
- 78 > 45, so maximum = 78 (remains largest)

---

### Problem 7: Find Both Min and Max in One Loop
**Question:** Find both smallest and largest using a single loop.

**Solution:**
```python
numbers = [45, 12, 78, 23, 9, 56]

minimum = numbers[0]
maximum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

print("Minimum:", minimum)
print("Maximum:", maximum)
```

**Output:**
```
Minimum: 9
Maximum: 78
```

**Explanation:**
- Initialize both with first element
- Check both conditions in the same loop
- More efficient than two separate loops

---

### Problem 8: Find Second Largest
**Question:** Find the second largest number without sorting.

**Solution:**
```python
numbers = [45, 12, 78, 23, 56, 89]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest:", second_largest)
```

**Output:** `Second largest: 78`

**Explanation:**
- Keep track of both largest and second_largest
- When you find a new largest, old largest becomes second_largest
- 89 is largest, 78 is second largest

---

### Problem 9: Find Difference Between Max and Min
**Question:** Find the difference without using `max()` or `min()`.

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

print("Difference:", difference)
```

**Output:** `Difference: 69`

**Explanation:**
- Find min: 9
- Find max: 78
- Difference: 78 - 9 = 69

---

## 📊 Counting and Filtering

### Problem 10: Count Even and Odd
**Question:** Count how many numbers are even and how many are odd.

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
- Use `%` operator to check remainder when dividing by 2
- If remainder is 0, number is even
- If remainder is 1, number is odd

---

### Problem 11: Count Positive and Negative
**Question:** Count positive and negative numbers.

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

---

### Problem 12: Filter Even Numbers
**Question:** Create a new list with only even numbers.

**Solution:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("Even numbers:", even_numbers)
```

**Output:** `Even numbers: [2, 4, 6, 8, 10]`

---

### Problem 13: Find Numbers Greater Than Value
**Question:** Find all numbers greater than a given value.

**Solution:**
```python
numbers = [10, 25, 30, 15, 40, 5]
threshold = 20

greater_numbers = []

for num in numbers:
    if num > threshold:
        greater_numbers.append(num)

print("Numbers greater than", threshold, ":", greater_numbers)
```

**Output:** `Numbers greater than 20 : [25, 30, 40]`

---

### Problem 14: Count Occurrences
**Question:** Count how many times a number appears without using `.count()`.

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

---

## 🔄 List Transformations

### Problem 15: Double Every Number
**Question:** Create a new list with each number doubled.

**Solution:**
```python
original = [1, 2, 3, 4, 5]

doubled = []

for num in original:
    doubled.append(num * 2)

print("Original:", original)
print("Doubled:", doubled)
```

**Output:**
```
Original: [1, 2, 3, 4, 5]
Doubled: [2, 4, 6, 8, 10]
```

---

### Problem 16: Square Each Number
**Question:** Create a new list with squares of each number.

**Solution:**
```python
numbers = [1, 2, 3, 4, 5]

squares = []

for num in numbers:
    squares.append(num ** 2)  # or num * num

print("Squares:", squares)
```

**Output:** `Squares: [1, 4, 9, 16, 25]`

---

### Problem 17: Reverse a List
**Question:** Reverse a list without using `reverse()` or slicing.

**Solution Method 1 (Using negative indexes):**
```python
numbers = [1, 2, 3, 4, 5]

reversed_list = []

# Count items
length = 0
for num in numbers:
    length = length + 1

# Add from end to beginning
for i in range(1, length + 1):
    reversed_list.append(numbers[-i])

print("Reversed:", reversed_list)
```

**Solution Method 2 (Using range backwards):**
```python
numbers = [1, 2, 3, 4, 5]

reversed_list = []

# Count items
length = 0
for num in numbers:
    length = length + 1

# Loop backwards
for i in range(length - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Reversed:", reversed_list)
```

**Output:** `Reversed: [5, 4, 3, 2, 1]`

---

### Problem 18: Swap First and Last
**Question:** Swap the first and last elements.

**Solution:**
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

**Alternative (using tuple unpacking):**
```python
numbers = [10, 20, 30, 40, 50]

numbers[0], numbers[-1] = numbers[-1], numbers[0]

print("After swap:", numbers)
```

**Output:** `After swap: [50, 20, 30, 40, 10]`

---

## 📝 String Lists

### Problem 19: Find Longest Word
**Question:** Find the longest word without using `max()`.

**Solution:**
```python
words = ["cat", "elephant", "dog", "butterfly"]

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)
```

**Output:** `Longest word: butterfly`

---

### Problem 20: Find Shortest Word
**Question:** Find the shortest word without using `min()`.

**Solution:**
```python
words = ["cat", "elephant", "dog", "butterfly"]

shortest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word

print("Shortest word:", shortest)
```

**Output:** `Shortest word: cat`

---

### Problem 21: Count Total Characters
**Question:** Count total characters across all words.

**Solution:**
```python
words = ["cat", "dog", "bird"]

total_chars = 0

for word in words:
    total_chars = total_chars + len(word)

print("Total characters:", total_chars)
```

**Output:** `Total characters: 10`

---

### Problem 22: Find Words Starting with Letter
**Question:** Find all words starting with a specific letter.

**Solution:**
```python
animals = ["cat", "dog", "cow", "chicken", "deer"]
letter = "c"

matching_words = []

for animal in animals:
    if animal[0] == letter:
        matching_words.append(animal)

print("Words starting with", letter, ":", matching_words)
```

**Output:** `Words starting with c : ['cat', 'cow', 'chicken']`

---

### Problem 23: Check if Word Exists
**Question:** Check if a word exists using a loop (not `in` keyword).

**Solution:**
```python
fruits = ["apple", "banana", "cherry", "date"]
search = "banana"

found = False

for fruit in fruits:
    if fruit == search:
        found = True

if found:
    print(search, "found in the list")
else:
    print(search, "not found in the list")
```

**Output:** `banana found in the list`

---

### Problem 24: Convert to Uppercase
**Question:** Create a new list with all words in uppercase.

**Solution:**
```python
words = ["hello", "world", "python"]

uppercase_words = []

for word in words:
    uppercase_words.append(word.upper())

print("Uppercase:", uppercase_words)
```

**Output:** `Uppercase: ['HELLO', 'WORLD', 'PYTHON']`

---

### Problem 25: Reverse Each Word
**Question:** Reverse each word in the list.

**Solution:**
```python
words = ["hello", "world", "python"]

reversed_words = []

for word in words:
    reversed_words.append(word[::-1])

print("Reversed words:", reversed_words)
```

**Output:** `Reversed words: ['olleh', 'dlrow', 'nohtyp']`

---

### Problem 26: Find Palindromes
**Question:** Find all palindrome words.

**Solution:**
```python
words = ["racecar", "hello", "level", "world", "noon"]

palindromes = []

for word in words:
    if word == word[::-1]:
        palindromes.append(word)

print("Palindromes:", palindromes)
```

**Output:** `Palindromes: ['racecar', 'level', 'noon']`

---

## 🎯 Advanced Problems

### Problem 27: Remove Duplicates
**Question:** Remove duplicate numbers without using `set()`.

**Solution:**
```python
numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = []

for num in numbers:
    # Check if already in unique list
    already_added = False
    for unique_num in unique_numbers:
        if num == unique_num:
            already_added = True
            break
    
    # Add only if not already there
    if not already_added:
        unique_numbers.append(num)

print("Unique numbers:", unique_numbers)
```

**Output:** `Unique numbers: [1, 2, 3, 4, 5]`

---

### Problem 28: Find Numbers Divisible by 3 and 5
**Question:** Find numbers divisible by both 3 AND 5.

**Solution:**
```python
numbers = [15, 20, 30, 45, 50, 60, 75]

divisible = []

for num in numbers:
    if num % 3 == 0 and num % 5 == 0:
        divisible.append(num)

print("Divisible by both 3 and 5:", divisible)
```

**Output:** `Divisible by both 3 and 5: [15, 30, 45, 60, 75]`

---

### Problem 29: Running Total
**Question:** Create a list showing running total at each position.

**Solution:**
```python
numbers = [1, 2, 3, 4, 5]

running_totals = []
total = 0

for num in numbers:
    total = total + num
    running_totals.append(total)

print("Running totals:", running_totals)
```

**Output:** `Running totals: [1, 3, 6, 10, 15]`

**Explanation:**
- After 1: total = 1
- After 2: total = 1 + 2 = 3
- After 3: total = 3 + 3 = 6
- After 4: total = 6 + 4 = 10
- After 5: total = 10 + 5 = 15

---

### Problem 30: Find Missing Number
**Question:** Find the missing number in a sequence from 1 to n.

**Solution:**
```python
numbers = [1, 2, 3, 5, 6, 7, 8, 9, 10]

# Calculate what the sum should be (1 to 10 = 55)
n = 10
expected_sum = (n * (n + 1)) // 2

# Calculate actual sum
actual_sum = 0
for num in numbers:
    actual_sum = actual_sum + num

# Missing number is the difference
missing = expected_sum - actual_sum

print("Missing number:", missing)
```

**Output:** `Missing number: 4`

**Explanation:**
- Sum of 1 to 10 should be: 55
- Actual sum: 1+2+3+5+6+7+8+9+10 = 51
- Missing: 55 - 51 = 4

---

### Problem 31: Temperature Analysis
**Question:** Analyze temperature data.

**Solution:**
```python
temperatures = [72, 78, 65, 80, 73, 68, 82, 75]

# Calculate average
total = 0
count = 0
for temp in temperatures:
    total = total + temp
    count = count + 1
average = total / count

# Find hottest
hottest = temperatures[0]
for temp in temperatures:
    if temp > hottest:
        hottest = temp

# Find coldest
coldest = temperatures[0]
for temp in temperatures:
    if temp < coldest:
        coldest = temp

# Count days above 75
above_75 = 0
for temp in temperatures:
    if temp > 75:
        above_75 = above_75 + 1

print("Average temperature:", average)
print("Hottest day:", hottest)
print("Coldest day:", coldest)
print("Days above 75°F:", above_75)
```

**Output:**
```
Average temperature: 74.125
Hottest day: 82
Coldest day: 65
Days above 75°F: 4
```

---

### Problem 32: Find Common Elements
**Question:** Find elements that appear in both lists.

**Solution:**
```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common = []

for num1 in list1:
    for num2 in list2:
        if num1 == num2:
            # Check if not already added
            already_in = False
            for item in common:
                if item == num1:
                    already_in = True
                    break
            
            if not already_in:
                common.append(num1)

print("Common elements:", common)
```

**Output:** `Common elements: [4, 5]`

---

## 📚 Common Mistakes to Avoid

### Mistake 1: Starting product with 0
❌ **Wrong:**
```python
product = 0  # Everything becomes 0!
for num in numbers:
    product = product * num
```

✅ **Correct:**
```python
product = 1  # Start with 1 for multiplication
for num in numbers:
    product = product * num
```

---

### Mistake 2: Forgetting to initialize variables
❌ **Wrong:**
```python
# total is not defined!
for num in numbers:
    total = total + num
```

✅ **Correct:**
```python
total = 0  # Initialize first!
for num in numbers:
    total = total + num
```

---

### Mistake 3: Modifying list while iterating
❌ **Wrong:**
```python
for num in numbers:
    if num < 0:
        numbers.remove(num)  # Can cause problems!
```

✅ **Correct:**
```python
new_list = []
for num in numbers:
    if num >= 0:
        new_list.append(num)
```

---

## 🎓 Teaching Tips

1. **Show the trace** - Walk through each step with values
2. **Use visual aids** - Draw boxes showing list contents
3. **Start simple** - Begin with 3-4 items, not 10
4. **Test edge cases** - Empty lists, single item, all same values
5. **Encourage debugging** - Use print statements to see values
6. **Compare methods** - Show multiple ways to solve

---

<div style="text-align: center; margin-top: 40px; padding: 20px; border-top: 2px solid #ccc;">
  <p><strong>MathCodeLab</strong> | Empowering Young Minds Through Code</p>
  <p>© 2025 MathCodeLab Team. All Rights Reserved.</p>
  <p><em>This Answer Key is for Instructors Only</em></p>
</div>
