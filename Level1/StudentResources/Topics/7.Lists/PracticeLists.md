# Practice Lists

Let's practice with lists! Here are comprehensive examples that match everything we learned in LearnLists.md. Work through each section step by step to become a list master!

## Section 1: Basic List Access

### Example 1: Storing Ages
This list keeps track of the ages of 5 kids. We use `print(ages[2])` to show the age of the third kid (remember, counting starts from 0!).
```python
ages = [7, 8, 9, 10, 11]
print(ages[2])  # Shows 9
print(ages[-1]) # Shows 11 (last item using negative index)
print(ages[1:4]) # Shows [8, 9, 10] (slicing)
```
**How does the output come?**
- `ages[2]` gets the item at index 2, which is 9
- `ages[-1]` counts backwards from the end, getting the last item (11)
- `ages[1:4]` gets items from index 1 to 3 (not including 4)

**Visual Representation:**
| Index | Value | Negative Index |
|-------|-------|----------------|
|   0   |   7   |      -5        |
|   1   |   8   |      -4        |
|   2   |   9   |      -3        |
|   3   |  10   |      -2        |
|   4   |  11   |      -1        |

### Example 2: Ice Cream Flavors with Advanced Access
This list shows different ways to access and modify ice cream flavors.
```python
flavors = ["chocolate", "vanilla", "strawberry", "mango"]
print(flavors[0])  # Shows 'chocolate'
flavors[2] = "mint"  # Change strawberry to mint
print(flavors)  # Shows ['chocolate', 'vanilla', 'mint', 'mango']

# Add new flavors
flavors.append("cookies")
flavors.insert(1, "caramel")
print(flavors)  # Shows ['chocolate', 'caramel', 'vanilla', 'mint', 'mango', 'cookies']
```
**How does the output come?**
- `flavors[0]` gets the first item: "chocolate"
- `flavors[2] = "mint"` changes the item at index 2 from "strawberry" to "mint"
- `append()` adds "cookies" to the end
- `insert(1, "caramel")` adds "caramel" at position 1, shifting others right

## Section 2: Different Ways to Loop Through Lists

### Example 3: Multiple Loop Methods
This example shows three different ways to loop through a list of stars:
```python
stars = [1, 2, 3, 4, 5]

# Method 1: Direct iteration
print("Method 1 - Direct:")
for star in stars:
    print("Star number:", star)

# Method 2: Using range and len (with index)
print("\nMethod 2 - With index:")
for i in range(len(stars)):
    print(f"Star at position {i}: {stars[i]}")

# Method 3: Using enumerate (gets both index and value)
print("\nMethod 3 - Index and value together:")
for i, star in enumerate(stars):
    print(f"Position {i} has star #{star}")
```
**Output:**
```
Method 1 - Direct:
Star number: 1
Star number: 2
Star number: 3
Star number: 4
Star number: 5

Method 2 - With index:
Star at position 0: 1
Star at position 1: 2
Star at position 2: 3
Star at position 3: 4
Star at position 4: 5

Method 3 - Index and value together:
Position 0 has star #1
Position 1 has star #2
Position 2 has star #3
Position 3 has star #4
Position 4 has star #5
```

## Section 3: Parallel Lists Practice

### Example 4: Days and Activities
This example shows how to work with parallel lists - two lists with related information:
```python
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
activities = ["Math Class", "Art Project", "Science Lab", "Reading", "Fun Friday"]

# Print each day with its activity
print("Weekly Schedule:")
for i in range(len(days)):
    print(f"{days[i]}: {activities[i]}")

# Find which day has Science Lab
for i in range(len(activities)):
    if activities[i] == "Science Lab":
        print(f"\nScience Lab is on {days[i]}")
        break

# Find all days with "F" in the activity name
print("\nActivities with 'F':")
for i in range(len(activities)):
    if "F" in activities[i]:
        print(f"{days[i]}: {activities[i]}")
```
**Output:**
```
Weekly Schedule:
Monday: Math Class
Tuesday: Art Project
Wednesday: Science Lab
Thursday: Reading
Friday: Fun Friday

Science Lab is on Wednesday

Activities with 'F':
Friday: Fun Friday
```

## Section 4: Comprehensive List Searching

### Example 5: Advanced Fruit Basket Operations
This example demonstrates multiple search and manipulation techniques:
```python
basket = ["apple", "banana", "orange", "apple", "grape"]

# Basic operations
print("Original basket:", basket)
basket.append("mango")
print("After adding mango:", basket)

# Searching techniques
print(f"\nIs 'apple' in basket? {'apple' in basket}")
print(f"How many apples? {basket.count('apple')}")
print(f"Position of first apple: {basket.index('apple')}")

# Find all fruits with 'a' in the name
fruits_with_a = []
for fruit in basket:
    if 'a' in fruit:
        fruits_with_a.append(fruit)
print(f"Fruits containing 'a': {fruits_with_a}")

# Find longest fruit name
longest_fruit = ""
for fruit in basket:
    if len(fruit) > len(longest_fruit):
        longest_fruit = fruit
print(f"Longest fruit name: {longest_fruit}")

# Remove an item
if "banana" in basket:
    basket.remove("banana")
    print(f"After removing banana: {basket}")
```

## Section 5: Mixed Data Types Practice

### Example 6: Student Information
Working with lists that contain different data types:
```python
# Student info: [name, age, grade, gpa, is_honor_student]
student = ["Alice Johnson", 10, "5th Grade", 3.8, True]

print(f"Student: {student[0]}")
print(f"Age: {student[1]} years old")
print(f"Grade: {student[2]}")
print(f"GPA: {student[3]}")
print(f"Honor Student: {student[4]}")

# Multiple students with parallel lists
names = ["Alice", "Bob", "Charlie", "Diana"]
ages = [10, 11, 9, 10]
gpas = [3.8, 3.2, 3.9, 3.6]
honor_students = [True, False, True, False]

print("\nClass Roster:")
for i in range(len(names)):
    honor_status = "Honor Student" if honor_students[i] else "Regular Student"
    print(f"{names[i]} (Age {ages[i]}): GPA {gpas[i]} - {honor_status}")

# Find all honor students
print("\nHonor Students:")
for i in range(len(names)):
    if honor_students[i]:
        print(f"- {names[i]} (GPA: {gpas[i]})")
```

---

# Practice Challenges

## Easy Level:
1. Create a list of your 5 favorite movies. Print the first and last movies using positive and negative indices.
2. Make a list of numbers [10, 20, 30, 40, 50]. Use slicing to print the middle three numbers.
3. Create two parallel lists: one with subject names and one with your grades. Print each subject with its grade.

## Medium Level:
4. Create a list of words. Find and print all words that contain the letter 'e'.
5. Make a list of temperatures [68, 72, 75, 69, 80, 77]. Find the hottest and coldest days with their positions.
6. Create a shopping list and prices list. Find all items under $5.00.

## Hard Level:
7. Create a list of names and a list of birth years. Calculate and display everyone's age (assume current year is 2025).
8. Make a list of mixed data types (numbers, strings, booleans). Count how many of each type you have.
9. Create a gradebook system: student names, test1 scores, test2 scores. Find the student with the highest average.

## Challenge Problem:
10. Create a mini library system with book titles, authors, and availability status (True/False). Write code that can:
    - List all available books
    - Find books by a specific author
    - "Check out" a book (change availability to False)
    - Find the author with the most books

---

## Quick Reference: List Methods You Should Know
```python
my_list = [1, 2, 3]
my_list.append(4)        # Add to end: [1, 2, 3, 4]
my_list.insert(0, 0)     # Insert at position: [0, 1, 2, 3, 4]
my_list.remove(2)        # Remove first occurrence: [0, 1, 3, 4]
my_list.count(1)         # Count occurrences: 1
my_list.index(3)         # Find position: 2
len(my_list)             # Get length: 4
```

Have fun practicing lists! Remember: lists are powerful tools that help you organize and work with lots of data efficiently!
