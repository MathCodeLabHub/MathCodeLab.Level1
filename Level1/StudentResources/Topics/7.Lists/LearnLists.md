# Lists

Lists are like boxes that help us store many things together. Imagine you have a box with 5 slots, and you can put a toy in each slot. That's what a list does in Python!

## Why Use Lists?
- To keep things organized
- To store lots of similar items (like numbers, names, or colors)
- To find things quickly

## How Does a List Look?

Here is a list with 5 numbers:

```
numbers = [2, 4, 6, 8, 10]
```

Each number is in a special place called an "index". The first place is index 0, the second is index 1, and so on.

| Index | Value |
|-------|-------|
|   0   |   2   |
|   1   |   4   |
|   2   |   6   |
|   3   |   8   |
|   4   |  10   |

## How to Use Lists?

### 1. Getting a Value
To get the first number:
```
print(numbers[0])  # Shows 2
```

### 2. Changing a Value
To change the third number to 12:
```
numbers[2] = 12
print(numbers)  # Now it's [2, 4, 12, 8, 10]
```

### 3. Looping Through a List
You can look at every item in the list using a loop:
```
for num in numbers:
    print(num)
```
This will print each number one by one.

### 4. More Ways to Access Elements

#### Index-Based Access with Range
Sometimes you need to know the position (index) while looping:
```
numbers = [2, 4, 6, 8, 10]
for i in range(len(numbers)):
    print(f"Index {i}: {numbers[i]}")
# Shows:
# Index 0: 2
# Index 1: 4
# Index 2: 6
# Index 3: 8
# Index 4: 10
```

#### Iterating Through Items (Direct Method)
This is the simplest way to go through each item:
```
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")
# Shows each fruit one by one
```

#### Using For Loop with Range for Index Access
When you need to know both the position and the value:
```
colors = ["red", "blue", "green", "yellow"]
for i in range(len(colors)):
    print(f"Color #{i+1}: {colors[i]}")
# Shows:
# Color #1: red
# Color #2: blue
# Color #3: green
# Color #4: yellow
```

#### Accessing Items with Negative Indices
You can count backwards from the end of the list:
```
pets = ["cat", "dog", "bird", "fish"]
print(pets[-1])    # Shows "fish" (last item)
print(pets[-2])    # Shows "bird" (second to last)
print(pets[-3])    # Shows "dog" (third to last)
```

#### Slicing Lists (Getting Multiple Items)
You can get a piece of a list using slicing:
```
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[1:4])    # Shows [20, 30, 40] (items 1, 2, 3)
print(numbers[:3])     # Shows [10, 20, 30] (first 3 items)
print(numbers[3:])     # Shows [40, 50, 60] (from item 3 to end)
print(numbers[::2])    # Shows [10, 30, 50] (every 2nd item)
```

### 5. Parallel Lists - Working with Related Data

Sometimes we have two lists that go together. The items in the same position are related to each other!

#### Example: Scores and Subjects
```
subjects = ["Math", "Science", "English", "History"]
scores = [95, 87, 92, 88]

# Print each subject with its score
for i in range(len(subjects)):
    print(f"{subjects[i]}: {scores[i]} points")

# Shows:
# Math: 95 points
# Science: 87 points
# English: 92 points
# History: 88 points
```

#### Example: Names and Ages
```
names = ["Alice", "Bob", "Charlie", "Diana"]
ages = [10, 11, 9, 10]

# Find who is 10 years old
for i in range(len(names)):
    if ages[i] == 10:
        print(f"{names[i]} is 10 years old")
        
# Shows:
# Alice is 10 years old
# Diana is 10 years old
```

#### Example: Cities and Temperatures
```
cities = ["New York", "Miami", "Seattle", "Denver"]
temperatures = [68, 82, 55, 70]

# Find the warmest city
hottest_temp = 0
hottest_city = ""

for i in range(len(cities)):
    if temperatures[i] > hottest_temp:
        hottest_temp = temperatures[i]
        hottest_city = cities[i]

print(f"The warmest city is {hottest_city} at {hottest_temp}°F")
# Shows: The warmest city is Miami at 82°F
```

### 6. Lists Can Hold Different Types
Python lists are very flexible and can hold the same type or mixed types:
```
# Same type - all numbers
scores = [95, 87, 92, 88]

# Mixed types - numbers and text together
student_info = ["Alice", 10, "Grade 5", 95.5]
# This works in Python! Each slot can hold different kinds of data.
```

## What About Arrays?

In Python, **lists** are what we use most of the time. Some other programming languages have strict "arrays" that can only hold one type of data, but Python lists are much more flexible!

### Python Lists Are Amazing Because:
- **Flexible**: Can store any type of data (numbers, text, even other lists!)
- **Easy to change**: Add or remove items anytime
- **Simple syntax**: Just use square brackets `[]`
- **Powerful methods**: Lots of built-in tools to work with data

### Cool List Methods You Can Try:
```
my_list = [1, 2, 3]
my_list.append(4)        # Add item to end: [1, 2, 3, 4]
my_list.insert(0, 0)     # Add item at beginning: [0, 1, 2, 3, 4]
my_list.remove(2)        # Remove the number 2: [0, 1, 3, 4]
print(len(my_list))      # Shows how many items: 4
```

## Fun Example: Storing Favorite Fruits
```
fruits = ["apple", "banana", "cherry", "grape"]
print(fruits[1])  # Shows 'banana'
```

## Why Lists Are Cool
- You can store lots of things without making many variables
- You can use loops to do things with all items
- Lists make your code neat and tidy!

## Searching in Lists

There are many ways to search for items in lists! Let's explore different search methods:

### 1. Check if Item Exists (Simple Search)
The easiest way to see if something is in your list:

```
fruits = ["apple", "banana", "cherry", "grape"]
if "banana" in fruits:
    print("Yes, banana is here!")
else:
    print("No banana found!")
```

### 2. Find the Position (Index) of an Item
Use `.index()` to find WHERE an item is located:

```
colors = ["red", "blue", "green", "yellow"]
position = colors.index("green")
print(f"Green is at position {position}")  # Shows: Green is at position 2

# Be careful! This gives an error if item isn't found
# Better to check first:
if "purple" in colors:
    position = colors.index("purple")
else:
    print("Purple not found in the list")
```

### 3. Count How Many Times Something Appears
Use `.count()` to see how many times an item appears:

```
numbers = [1, 2, 3, 2, 4, 2, 5]
how_many_twos = numbers.count(2)
print(f"The number 2 appears {how_many_twos} times")  # Shows: 3 times

letters = ["a", "b", "c", "a", "d", "a"]
print(f"Letter 'a' appears {letters.count('a')} times")  # Shows: 3 times
```

### 4. Search with Conditions (Using Loops)
Find items that meet certain conditions:

```
ages = [8, 12, 7, 15, 9, 13, 6]

# Find all ages greater than 10
older_kids = []
for age in ages:
    if age > 10:
        older_kids.append(age)
print("Ages over 10:", older_kids)  # Shows: [12, 15, 13]

# Count how many are older than 10
count = 0
for age in ages:
    if age > 10:
        count += 1
print(f"Number of kids over 10: {count}")  # Shows: 3
```

### 5. Search in Strings Within Lists
Find words that contain certain letters:

```
animals = ["cat", "dog", "elephant", "tiger", "rabbit"]

# Find animals with 'a' in their name
animals_with_a = []
for animal in animals:
    if "a" in animal:
        animals_with_a.append(animal)
print("Animals with 'a':", animals_with_a)  # Shows: ['cat', 'elephant', 'rabbit']

# Find animals with exactly 3 letters
short_animals = []
for animal in animals:
    if len(animal) == 3:
        short_animals.append(animal)
print("3-letter animals:", short_animals)  # Shows: ['cat', 'dog']
```

### 6. Find the First Item That Matches
Sometimes you want to find the FIRST item that meets a condition:

```
scores = [65, 78, 45, 89, 92, 73]

# Find the first score above 80
first_high_score = None
for score in scores:
    if score > 80:
        first_high_score = score
        break  # Stop looking once we find one!

if first_high_score:
    print(f"First high score: {first_high_score}")  # Shows: 89
else:
    print("No high scores found")
```

### 7. Search with Position Information
Find items AND remember where they are:

```
temperatures = [68, 72, 75, 69, 80, 77]
hot_days = []

for i in range(len(temperatures)):
    if temperatures[i] > 75:
        hot_days.append(f"Day {i+1}: {temperatures[i]}°F")

print("Hot days:")
for day in hot_days:
    print(day)
# Shows:
# Day 5: 80°F
# Day 6: 77°F
```

### 8. Advanced Search: Find Maximum and Minimum
Find the biggest and smallest items:

```
test_scores = [87, 92, 78, 95, 83, 90]

# Find highest score and who got it (using parallel lists)
students = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]

highest_score = 0
best_student = ""

for i in range(len(test_scores)):
    if test_scores[i] > highest_score:
        highest_score = test_scores[i]
        best_student = students[i]

print(f"Highest score: {highest_score} by {best_student}")
# Shows: Highest score: 95 by Diana
```

### 9. Search Multiple Lists at Once
Search across parallel lists for related information:

```
products = ["Apple", "Banana", "Orange", "Grapes"]
prices = [1.50, 0.75, 2.00, 3.25]

# Find products under $2.00
affordable_products = []
for i in range(len(products)):
    if prices[i] < 2.00:
        affordable_products.append(f"{products[i]}: ${prices[i]}")

print("Affordable products:")
for product in affordable_products:
    print(product)
# Shows:
# Apple: $1.5
# Banana: $0.75
```

### Try These Search Challenges!
1. Create a list of your friends' names and find all names that start with the same letter as yours
2. Make a list of numbers and find all numbers that are divisible by 3
3. Create two lists (book titles and ratings) and find all books with ratings above 4.0
4. Search for the longest word in a list of words

## Filtering Lists
Filtering means picking only the items you want from a list. For example, let's pick only the even numbers from a list:

```
numbers = [2, 4, 6, 8, 10, 11, 13]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)  # Shows [2, 4, 6, 8, 10]
```
Now, even_numbers only has the even numbers from the original list.


## Try It Yourself!
- Make a list of your favorite colors
- Print the first color
- Change the last color to something new
- Search for your favorite color in the list and print if it is found
- Make a list of numbers and filter out only the even numbers

---
Lists are super useful and fun. You will use them a lot as you learn more about programming!
