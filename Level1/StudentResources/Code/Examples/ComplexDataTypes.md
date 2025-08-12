<img src="../../../../CommonResources/Logo.MathCodeLab.Light.png#gh-light-mode-only" alt="MathCodeLab" width="200"/>
<img src="../../../../CommonResources/Logo.MathCodeLab.Dark.jpg#gh-dark-mode-only" alt="MathCodeLab" width="200"/>

## Topics Covered
1. Complex built-in data types – examples of lists, tuples, ranges, dictionaries, and sets.
2. Converting between types – converting sequences of strings to numbers.
3. Looping through lists – iterating over lists.
4. Break and continue with lists – controlling loops with lists.
5. Nested loops – creating combinations with multiple lists.
6. More range patterns – converting ranges to lists and counting backwards.
7. Membership and identity operators – using `in`, `not in`, `is`, and `is not`.

---

## Example 1: Complex built-in data types
```python
# We include both simple and complex types to compare them.
text       = "Goodbye"
integer    = 99
decimal    = 1.618
complex_no = 1 + 2j
my_list    = ["dog", "cat", "mouse"]
my_tuple   = (4, 5, 6)
my_range   = range(3, 8)
my_dict    = {"city": "Seattle", "population": 700000}
my_set     = {"red", "green", "blue"}
truth      = False
nothing    = None

print("Example 1: Data types and their types")
for item in [text, integer, decimal, complex_no, my_list, my_tuple,
             my_range, my_dict, my_set, truth, nothing]:
    print(item, "is of type", type(item))
```

## Example 2: Converting between types using constructor functions
```python
nums_as_strings = list(("4", "6", "8"))
nums_as_ints    = [int(n) * 2 for n in nums_as_strings]  # convert each to int and double the value
print("Example 2:")
print("Original strings:", nums_as_strings)
print("Converted and doubled:", nums_as_ints)
```

## Example 3: Looping through a list
```python
colors = ["red", "green", "blue"]
print("Example 3:")
for color in colors:
    print("I like", color)
```

## Example 4: Break and continue in a for loop with a list
```python
animals = ["lion", "tiger", "bear", "zebra"]
print("Example 4:")
for animal in animals:
    if animal == "bear":
        print("Found the bear, stopping early!")
        break  # stop the loop when we reach 'bear'
    if animal == "tiger":
        print("Skipping the tiger!")
        continue  # skip printing 'tiger'
    print("Current animal:", animal)
```

## Example 5: Nested loops to create combinations
```python
adjectives = ["small", "fast", "shiny"]
vehicles    = ["car", "bike", "plane"]
print("Example 5:")
for adj in adjectives:
    for vehicle in vehicles:
        print(adj, vehicle)
```

## Example 6: More range patterns
```python
print("Example 6:")
# Create a list of even numbers from 0 up to (but not including) 10
evens = list(range(0, 10, 2))
print("Even numbers from 0 to 8:", evens)

# Count down from 5 to 1 using a negative step
print("Countdown:")
for i in range(5, 0, -1):
    print(i)
```

## Example 7: Membership and identity operators
```python
print("Example 7:")
numbers_list = [5, 10, 15]
print("10 in numbers_list ->", 10 in numbers_list)
print("7 not in numbers_list ->", 7 not in numbers_list)

# Identity vs equality
a = [1, 2, 3]
b = a            # b references the same list as a
c = [1, 2, 3]    # c is a new list with the same contents as a

print("a == c ->", a == c)   # values are equal
print("b is a ->", b is a)   # b and a refer to the same object
print("c is a ->", c is a)   # c is a separate object
```
---
© 2025 MathCodeLab Team. All Rights Reserved.