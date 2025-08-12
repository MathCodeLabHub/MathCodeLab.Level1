<img src="../../../../CommonResources/Logo.MathCodeLab.Light.png#gh-light-mode-only" alt="MathCodeLab" width="200"/>
<img src="../../../../CommonResources/Logo.MathCodeLab.Dark.jpg#gh-dark-mode-only" alt="MathCodeLab" width="200"/>

## Topics Covered
1. Variables and values – creating and assigning variables.
2. Simple data types – strings, integers, floats, complex numbers, booleans, and None.
3. Operators – arithmetic, comparison, logical, and swapping values.
4. Conditional statements – if, elif, and else.
5. Loops – for and while loops with numbers and strings, including range-based counting, break/continue, else clauses, and a challenge to find divisible numbers.
6. Strings – concatenation and repetition.

---

## Example 1: Creating and printing simple variables
```python
x = 10              # integer
y = "Alice"         # string
print("Example 1:")
print(x)
print(y)

# Now change x to another string and print again.  Notice that
# Python doesn’t mind if a variable changes type.
x = "Bob"
print("x is now:", x)
```

## Example 2: Assigning multiple variables in one line
```python
a, b, c = 7, 3.14, "apples"   # a is int, b is float, c is string
print("Example 2:")
print("a =", a, "b =", b, "c =", c)

# You can also assign the same value to multiple variables in one line.
p = q = r = "common"
print("p =", p, "q =", q, "r =", r)
```

## Example 3: Casting variables to specify data types
```python
m = str(10)       # m will be the string '10'
n = int("42")     # n will be the integer 42 (converted from string)
o = float("2.718") # o will be the floating point number 2.718
print("Example 3:")
print("m:", m, type(m))
print("n:", n, type(n))
print("o:", o, type(o))
```

## Example 4: Simple data types
```python
text    = "Goodbye"
integer = 99
decimal = 1.618
complex_no = 1 + 2j
truth   = False
nothing = None

print("Example 4: Simple data types and their types")
for item in [text, integer, decimal, complex_no, truth, nothing]:
    print(item, "is of type", type(item))
```

## Example 5: Basic arithmetic operators
```python
a = 7
b = 4
print("Example 5:")
print("a + b =", a + b)    # addition
print("a - b =", a - b)    # subtraction
print("a * b =", a * b)    # multiplication
print("a / b =", a / b)    # division (float)
print("a ** b =", a ** b)  # exponentiation
print("a // b =", a // b)  # floor division
print("a % b =", a % b)    # modulus (remainder)
```

## Example 6: Comparison operators
```python
x = 12
y = 6
print("Example 6:")
print("x == y ->", x == y)   # equality
print("x != y ->", x != y)   # not equal
print("x < y  ->", x < y)    # less than
print("x <= y ->", x <= y)   # less than or equal
print("x > y  ->", x > y)    # greater than
print("x >= y ->", x >= y)   # greater than or equal
```

## Example 7: Logical operators
```python
p = True
q = False
print("Example 7:")
print("p and q ->", p and q)  # both must be True
print("p or q  ->", p or q)   # either can be True
print("not p   ->", not p)    # invert the Boolean value
```

## Example 8: Swapping variable values
```python
# You can swap two variables in Python without using a temporary variable.
m = "sun"
n = "moon"
print("Example 8:")
print("Before swap: m =", m, ", n =", n)

o = n
n = m
m = o  # Using a temporary variable also works.
print("After swap using temp:  m =", m, ", n =", n)

m, n = n, m  # simultaneous assignment swaps the values
print("After swap with simultaneous assignment:  m =", m, ", n =", n)

# Using a temporary variable also works.
x_var = 10
y_var = 20
print("Swapping using a temporary variable: before: x =", x_var, ", y =", y_var)

temp = x_var
x_var = y_var
y_var = temp
print("after: x =", x_var, ", y =", y_var)

x_var, y_var = y_var, x_var  # simultaneous assignment swaps the values
print("after: x =", x_var, ", y =", y_var)
```

## Example 9: Simple if statement
```python
number = 42
print("Example 9:")
# Check if the number is even
if number % 2 == 0:
    print(number, "is an even number!")
print("This line always prints.")
```

## Example 10: if-else statement
```python
grade = 85
print("Example 10:")
if grade >= 90:
    print("Excellent work!")
else:
    print("Keep studying, you'll improve!")
```

## Example 11: if-elif-else chain
```python
score = 78
print("Example 11:")
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade D or F")
```

## Example 12: Nested conditions and logical operators
```python
n = 15
print("Example 12:")
if n > 0:
    print(n, "is positive")
elif n < 0:
    print(n, "is negative")
else:
    print(n, "is zero")

# Check even/odd only if n is not zero
if n != 0:
    if n % 2 == 0:
        print("and it is even")
    else:
        print("and it is odd")
```

## Example 13: Looping through a string
```python
word = "Python"
print("Example 13:")
for letter in word:
    print(letter)
```

## Example 14: Using range() to count
```python
print("Example 14:")
for i in range(1, 4):  # counts 1,2,3
    print(i)

# Start and stop parameters
print("Counting from 3 to 6:")
for i in range(3, 7):  # counts 3,4,5,6
    print(i)

# Step parameter to skip numbers
print("Counting by fours:")
for i in range(0, 13, 4):
    print(i)
```

## Example 15: Else clause on a for loop
```python
print("Example 15:")
for i in range(3):
    print(i)
else:
    print("Loop finished!")

print("Demonstrating that else does not run when break is used:")
for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("This will not print because of the break")
```

## Example 16: Basic while loop
```python
counter = 0
print("Example 16:")
while counter < 4:
    print("Counter is", counter)
    counter += 1  # increment to eventually end the loop
```

## Example 17: Using break and continue in a while loop
```python
i = 0
print("Example 17:")
while i < 6:
    i += 1
    if i == 3:
        print("Skipping 3!")
        continue
    if i == 5:
        print("Found 5, breaking out!")
        break
    print("Current value:", i)
```

## Example 18: While loop with an else clause
```python
j = 2
print("Example 18:")
while j < 6:
    print("j is", j)
    j += 1
else:
    print("j is no longer less than 6 – loop complete!")
```

## Example 19: Fun string operators
```python
print("Example 19:")
greeting = "Good" + "bye"
print(greeting)

syllable = "yo"
repeat_word = syllable * 4
print("When you multiply 'yo' by 4 you get:", repeat_word)
```

## Example 20: Combining loops and conditions
```python
print("Example 20:")
for num in range(1, 25):
    # Print numbers that are multiples of 4 or 6
    if num % 4 == 0 or num % 6 == 0:
        print(num, "is divisible by 4 or 6")
```

---
© 2025 MathCodeLab Team. All Rights Reserved.
