<div align="center">
<img src="../../../CommonResources/Logo.MathCodeLab.Light.png#gh-light-mode-only" alt="MathCodeLab" width="150"/>
<img src="../../../CommonResources/Logo.MathCodeLab.Dark.jpg#gh-dark-mode-only" alt="MathCodeLab" width="150"/>
</div>

# MCL.Level1.Loops – Puzzle-Based Programming Solutions & Explanations 🧠🐍

Complete solutions with detailed explanations for the four puzzle-based programming problems. Each solution demonstrates key programming concepts in an engaging way.

---

## 🔐 **Problem 1: Magic Number Lock - SOLUTION**

### **Understanding the Problem**
We need a number that is:
- ✅ Divisible by 3 (remainder = 0 when divided by 3)
- ✅ Divisible by 5 (remainder = 0 when divided by 5)  
- ❌ NOT divisible by 2 (remainder ≠ 0 when divided by 2, i.e., ODD)

**Key Insight:** Numbers divisible by both 3 and 5 are divisible by 15. So we need odd multiples of 15: 15, 45, 75, 105, etc.

### **Solution Code**
```python
# Magic Number Lock program
number = int(input("Enter a number to test the magic lock: "))

# Check if number follows the magic rule
if number % 3 == 0 and number % 5 == 0 and number % 2 != 0:
    print(f"🎉 Treasure chest opens! {number} follows the magic rule!")
else:
    print(f"❌ Chest stays locked! {number} doesn't follow the magic rule.")
    
    # Optional: Explain why it failed using simple if statements
    print("Reason:", end=" ")
    if number % 3 != 0:
        print(f"{number} is not divisible by 3", end="")
    if number % 5 != 0:
        if number % 3 != 0:
            print(" and ", end="")
        print(f"{number} is not divisible by 5", end="")
    if number % 2 == 0:
        if number % 3 != 0 or number % 5 != 0:
            print(" and ", end="")
        print(f"{number} is divisible by 2 (even)", end="")
    print(".")
```

### **Alternative Solution (More Concise)**
```python
# More concise version
number = int(input("Enter a number: "))

if number % 15 == 0 and number % 2 != 0:  # Divisible by 15 and odd
    print(f"🎉 Treasure opens! {number} is magic!")
else:
    print(f"❌ Chest locked! {number} is not magic.")
```

### **Test Results**
- 15: ✅ Opens (15÷3=5, 15÷5=3, 15÷2=7.5)
- 30: ❌ Locked (even number)
- 45: ✅ Opens (45÷3=15, 45÷5=9, 45÷2=22.5)
- 21: ❌ Locked (not divisible by 5)
- 75: ✅ Opens (75÷3=25, 75÷5=15, 75÷2=37.5)
- 90: ❌ Locked (even number)

---

## ⭐ **Problem 2: Star Pyramid Challenge - SOLUTION**

### **Understanding the Problem**
We need to print a pyramid where:
- Row 1: 1 star
- Row 2: 2 stars
- Row 3: 3 stars
- Row n: n stars

**Key Insight:** Use a loop to control rows, and for each row, print the correct number of stars.

### **Solution Code**
```python
# Star Pyramid program
n = int(input("Enter the height of the pyramid: "))

# Build the pyramid row by row
for row in range(1, n + 1):
    # Print 'row' number of stars
    stars = "*" * row
    print(stars)
```

### **Alternative Solution (More Explicit)**
```python
# More explicit version showing the loop clearly
n = int(input("Enter the height of the pyramid: "))

for row in range(1, n + 1):
    # Print stars one by one for this row
    for star in range(row):
        print("*", end="")  # end="" prevents newline
    print()  # Move to next line after each row
```

### **Step-by-Step Example (n=5)**
```
Row 1: range(1) → print 1 star  → *
Row 2: range(2) → print 2 stars → **
Row 3: range(3) → print 3 stars → ***
Row 4: range(4) → print 4 stars → ****
Row 5: range(5) → print 5 stars → *****
```

### **🌟 Bonus Solutions**

**Reverse Pyramid:**
```python
n = int(input("Enter the height: "))
for row in range(n, 0, -1):  # Count down from n to 1
    print("*" * row)
```

**Diamond Pattern:**
```python
n = int(input("Enter the size: "))
# Upper half (including middle)
for row in range(1, n + 1):
    print("*" * row)
# Lower half
for row in range(n - 1, 0, -1):
    print("*" * row)
```

---

## 🔍 **Problem 3: Guess the Data Type - SOLUTION**

### **Understanding the Problem**
We need to determine if user input represents:
- **Integer**: Whole numbers (42, -17, 0)
- **Float**: Decimal numbers (3.14, 123.0, -5.5)
- **String**: Text that can't be converted to numbers (Hello, abc123)

**Key Insight:** Use string methods to analyze the input without advanced error handling.

### **Solution Code (String Analysis Method)**
```python
# Data Type Detective program using basic checks
user_input = input("Enter something and I'll guess its type: ")

# Simple type detection using basic string methods
# Check if it's a float first (contains decimal point)
if '.' in user_input:
    print(f"That's a float! 🔢.🔢")
    
# Check if it's a negative integer (contains minus sign)
elif '-' in user_input:
    print(f"That's an integer! 🔢")
    print("   └─ It's negative!")
    
# Check if it's a positive integer
elif user_input.isdigit():
    print(f"That's an integer! 🔢")
    print("   └─ It's positive!")
    
# Everything else is a string
else:
    print(f"That's a string! 📝")
```

### **Alternative Solution (Simplified)**
```python
# Simpler version focusing on basic cases
user_input = input("Enter something: ")

# Check for decimal point first
if '.' in user_input:
    print("That's a float! 🔢.🔢")
# Check if it's a negative integer (contains minus sign)
elif '-' in user_input:
    print("That's an integer! 🔢")
# Check if all characters are digits
elif user_input.isdigit():
    print("That's an integer! 🔢")
else:
    print("That's a string! 📝")
```

### **Test Results**
- "42" → Integer (42)
- "3.14" → Float (3.14)  
- "Hello" → String ('Hello')
- "123.0" → Float (123.0)
- "-57" → Integer (-57)
- "0" → Integer (0)

---

## 🤖 **Problem 4: Robot Steps Puzzle - SOLUTION**

### **Understanding the Problem**
Robot movement rules:
- **Odd step numbers** (1, 3, 5, ...): Move +3 steps
- **Even step numbers** (2, 4, 6, ...): Move +2 steps

**Key Insight:** Use a loop to simulate each move, check if move number is odd/even using modulo.

### **Solution Code**
```python
# Robot Steps program
n = int(input("How many moves should the robot make? "))

position = 0  # Robot starts at position 0

print(f"🤖 Robot starting at position: {position}")
print()

# Simulate each move
for move in range(1, n + 1):
    if move % 2 == 1:  # Odd move number
        steps = 3
        position += steps
        print(f"Move {move} (odd): +{steps} steps → Position: {position}")
    else:  # Even move number
        steps = 2
        position += steps
        print(f"Move {move} (even): +{steps} steps → Position: {position}")

print()
print(f"🤖 Robot's final position: {position}")
```

### **Alternative Solution (More Compact)**
```python
# More compact version using simple if-else
n = int(input("Number of moves: "))
position = 0

for move in range(1, n + 1):
    # Check if move number is odd or even
    if move % 2 == 1:  # Odd move
        steps = 3
        move_type = "odd"
    else:  # Even move
        steps = 2
        move_type = "even"
    
    position += steps
    print(f"Move {move} ({move_type}): +{steps} → Position: {position}")

print(f"\n🤖 Final position: {position}")
```

### **Solution with Mathematical Formula**
For those interested in the math, we can calculate the final position directly:

```python
# Mathematical approach (advanced)
n = int(input("Number of moves: "))

# Count odd and even moves
odd_moves = (n + 1) // 2  # Ceiling division for odd count
even_moves = n // 2       # Floor division for even count

final_position = odd_moves * 3 + even_moves * 2
print(f"🤖 Final position (calculated): {final_position}")

# Verify with simulation
position = 0
for move in range(1, n + 1):
    if move % 2 == 1:  # Odd move
        position += 3
    else:  # Even move
        position += 2
print(f"🤖 Final position (simulated): {position}")
```

### **Step-by-Step Examples**

**Example 1: n = 5**
```
Move 1 (odd): +3 → Position: 3
Move 2 (even): +2 → Position: 5  
Move 3 (odd): +3 → Position: 8
Move 4 (even): +2 → Position: 10
Move 5 (odd): +3 → Position: 13
Final: 13
```

**Example 2: n = 6**
```
Move 1 (odd): +3 → Position: 3
Move 2 (even): +2 → Position: 5
Move 3 (odd): +3 → Position: 8
Move 4 (even): +2 → Position: 10
Move 5 (odd): +3 → Position: 13
Move 6 (even): +2 → Position: 15
Final: 15
```

### **Pattern Analysis**
- **n = 1**: 3
- **n = 2**: 5  
- **n = 3**: 8
- **n = 4**: 10
- **n = 5**: 13
- **n = 6**: 15

**Formula**: Final position = 3 × (odd_moves) + 2 × (even_moves)

---

## 🎯 **Teaching Notes & Extensions**

### **Key Concepts Reinforced**
1. **Modulo Operator (%)**: Checking divisibility and odd/even numbers
2. **Conditional Logic**: Using if/elif/else with complex conditions
3. **Loops**: Controlling repetition and iteration
4. **String Operations**: Multiplication (`"*" * n`) and concatenation
5. **Type Conversion**: int(), float(), and error handling
6. **Problem Decomposition**: Breaking complex problems into steps

### **Common Student Mistakes & Solutions**
1. **Forgetting `range(1, n+1)`**: Students often use `range(n)` which starts at 0
2. **Modulo Confusion**: Mixing up `%` for remainder vs division
3. **String vs Numeric Input**: Not converting input() to int/float when needed
4. **Off-by-one Errors**: In loop ranges and indexing

### **Extension Ideas**
1. **Magic Lock**: Find all magic numbers in a range, create different magic rules
2. **Pyramid**: Centered pyramids, hollow pyramids, number pyramids
3. **Data Type**: Handle edge cases like scientific notation, hexadecimal
4. **Robot**: Add backward movement, obstacles, or 2D movement

### **Assessment Rubric**
- **Code Functionality** (40%): Does the program work correctly?
- **Logic & Algorithm** (30%): Is the approach sound and efficient?
- **Code Quality** (20%): Clean, readable code with good variable names
- **Testing & Edge Cases** (10%): Did they test various inputs?

---

**These puzzles successfully combine fundamental programming concepts with engaging, game-like scenarios that motivate students to think algorithmically while having fun!** 🚀
