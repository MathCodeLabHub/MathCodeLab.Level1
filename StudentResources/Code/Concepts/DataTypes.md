<img src="../../../RepoResources/Logo.MathCodeLab.Light.png#gh-light-mode-only" alt="MathCodeLab" width="200"/>
<img src="../../../RepoResources/Logo.MathCodeLab.Dark.jpg#gh-dark-mode-only" alt="MathCodeLab" width="200"/>

# Python Data Types in Math Code Lab

This document provides a comprehensive overview of Python data types, organized by categories. Understanding these data types is fundamental to Python programming.

## Table of Contents
1. [Primitive Data Types](#1-primitive-data-types-built-in)
   - [String (str)](#string-str)
   - [Integer (int)](#integer-int)
   - [Float (Decimal)](#float-decimal)
   - [Boolean (bool)](#boolean-bool)
   - [None](#none)

2. [Complex Data Types](#2-complex-data-types-built-in)
   - [List](#list)
   - [Tuple](#tuple)
   - [Dictionary](#dictionary)
   - [Set](#set)
   - [Range](#range)

3. [User-Defined Data Types](#3-user-defined-data-types)
   - [Classes](#classes)
   - [Custom Collections](#custom-collections)

4. [Additional Resources](#additional-resources)
   - [Type Conversion](#type-conversion)
   - [Best Practices](#best-practices)

📝 **Note**: For hands-on examples, check out:
- [Simple Data Types Examples](./Examples/PrimitiveDataTypes.py)
- [Complex Data Types Examples](./Examples/ComplexDataTypes.py)

## 1. Primitive Data Types (Built-in)

### String (str)
- **What**: Text data of any length
- **Why Important**: 
  - Handles all text-based information (names, messages, commands)
  - Supports rich operations like splitting, joining, and pattern matching
- **Real Examples**:
  ```python
  name = "Alice"              # Store names
  message = "Hello, World!"   # Display messages
  path = "C:/Users/docs.txt"  # File paths
  ```

### Integer (int)
- **What**: Whole numbers without decimal points
- **Why Important**:
  - Perfect for counting and indexing
  - Used in mathematical calculations
  - Memory efficient for whole numbers
- **Real Examples**:
  ```python
  age = 25            # Ages
  count = 100         # Counting items
  position = -3       # Positions (including negative)
  ```

### Float (Decimal)
- **What**: Numbers with decimal points
- **Why Important**:
  - Essential for precise calculations
  - Required for scientific computations
  - Handles fractional values
- **Real Examples**:
  ```python
  temperature = 98.6  # Body temperature
  pi = 3.14159       # Mathematical constants
  price = 19.99      # Money values
  ```

### Boolean (bool)
- **What**: True/False values
- **Why Important**:
  - Controls program flow
  - Makes decisions in code
  - Essential for conditional logic
- **Real Examples**:
  ```python
  is_active = True    # Status flags
  has_permission = False  # Access control
  ```

### None
- **What**: Represents absence of value
- **Why Important**:
  - Initializes variables
  - Indicates "not yet set" state
  - Default return for functions
- **Real Examples**:
  ```python
  result = None      # Initialize before processing
  error = None       # No error state
  ```

## 2. Complex Data Types (Built-in)

For detailed examples and practice exercises, refer to [Complex Data Types Document](../ComplexDataTypes-Operators-Conditions-Loops/MCL.Level1.CDT.md).

### List
- **What**: Think of a list like a shopping list or a playlist:
  - It's like a container where you can store many items in order
  - You can add new items, remove items, or change items
  - Each item has a position number (starting at 0)
  - Just like how you can add songs to a playlist or cross items off a shopping list
  - Example: `my_games = ["Minecraft", "Roblox", "Pokemon"]`
- **Why Important**:
  - Dynamic size (can grow or shrink)
  - Supports item modification after creation
  - Maintains insertion order
  - Allows duplicate elements
  - Supports slicing and indexing
- **Real-World Applications**:
  - Shopping cart items
  - Task management (todo lists)
  - Student grades in a course
  - Browser history
- **Common Operations**:
  ```python
  # Creating and modifying lists
  grades = [95, 88, 92, 78]
  grades.append(85)          # Add new grade
  grades[0] = 97            # Modify first grade
  
  # List operations
  average = sum(grades) / len(grades)
  highest = max(grades)
  grades.sort(reverse=True)  # Sort descending
  
  # List comprehension
  passing_grades = [g for g in grades if g >= 60]
  ```

### Tuple
- **What**: Think of a tuple like a sealed package:
  - Once you create it, you can't add, remove, or change items inside
  - It's like a box of crayons with a fixed set of colors
  - Perfect for things that shouldn't change, like the days of the week
  - Always keeps items in the same order
  - Example: `days = ("Monday", "Tuesday", "Wednesday")`
- **Why Important**:
  - Protects data from accidental changes
  - More memory efficient than lists
  - Can be used as dictionary keys
  - Perfect for representing fixed collections
- **Real-World Applications**:
  - Geographic coordinates (latitude, longitude)
  - RGB color values
  - Database records
  - Function return values with multiple items
- **Common Operations**:
  ```python
  # Creating and using tuples
  point3D = (23.5, 42.1, 15.7)
  x, y, z = point3D         # Tuple unpacking
  
  # Named tuples for clarity
  from collections import namedtuple
  Point = namedtuple('Point', ['x', 'y', 'z'])
  location = Point(23.5, 42.1, 15.7)
  print(location.x)  # Access by name
  ```

### Dictionary
- **What**: Think of a dictionary like a contact list in your phone:
  - Each contact (key) has its own information (value)
  - Just like how each name in your contacts has a phone number
  - Keys must be unique (like how each person has their own contact entry)
  - You can look up information quickly using the key
  - Example: 
    ```python
    my_pet = {
        "name": "Fluffy",
        "type": "cat",
        "age": 3,
        "favorite_food": "tuna"
    }
    ```
- **Why Important**:
  - Fast lookups by key (O(1) complexity)
  - Each key must be unique
  - Values can be any type
  - Keys must be immutable
  - Maintains insertion order (Python 3.7+)
- **Real-World Applications**:
  - User profiles
  - Configuration settings
  - Caching systems
  - Language translation mappings
  - HTTP headers
- **Common Operations**:
  ```python
  # Creating and using dictionaries
  user = {
      'username': 'alice_dev',
      'email': 'alice@example.com',
      'active': True,
      'login_count': 42
  }
  
  # Dictionary operations
  user['last_login'] = '2025-08-07'  # Add new key-value
  email = user.get('email', 'No email found')  # Safe get
  
  # Dictionary comprehension
  uppercase_dict = {k: v.upper() for k, v in user.items() 
                   if isinstance(v, str)}
  ```

### Set
- **What**: Think of a set like a sticker collection:
  - You can't have duplicate stickers (each item appears only once)
  - It doesn't matter what order the stickers are in
  - It's easy to check if you have a specific sticker
  - Perfect for keeping track of things you have or haven't done
  - Example: 
    ```python
    # Collection of unique Pokemon cards
    my_cards = {"Pikachu", "Charizard", "Mewtwo"}
    # Set of completed game levels
    completed_levels = {"Level 1", "Level 2", "Boss Fight"}
    ```
- **Why Important**:
  - Automatically eliminates duplicates
  - Very fast membership testing
  - Supports mathematical set operations
  - Items must be immutable
- **Real-World Applications**:
  - Unique visitor tracking
  - Remove duplicates from data
  - Tag systems
  - Permission systems
  - Network connections
- **Common Operations**:
  ```python
  # Creating and using sets
  active_users = {'alice', 'bob', 'charlie'}
  premium_users = {'alice', 'david'}
  
  # Set operations
  all_users = active_users | premium_users  # Union
  premium_active = active_users & premium_users  # Intersection
  regular_users = active_users - premium_users  # Difference
  
  # Membership testing
  if 'alice' in active_users:  # Very fast operation
      print('Alice is active')
  ```

### Range
- **What**: Think of range like a number pattern machine:
  - It creates a sequence of numbers following a pattern
  - Like counting by 2s: 2, 4, 6, 8, ...
  - Or counting backwards: 10, 9, 8, 7, ...
  - Saves memory because it only remembers the pattern, not all the numbers
  - Examples:
    ```python
    # Counting from 1 to 5
    counting = range(1, 6)  # Makes: 1, 2, 3, 4, 5
    
    # Counting by 2s up to 10
    even_numbers = range(0, 11, 2)  # Makes: 0, 2, 4, 6, 8, 10
    
    # Counting backwards from 5 to 1
    countdown = range(5, 0, -1)  # Makes: 5, 4, 3, 2, 1
    ```
- **Why Important**:
  - Memory efficient (only stores start, stop, step)
  - Perfect for counting and iteration
  - Commonly used in for loops
  - Generates numbers on demand
- **Real-World Applications**:
  - Pagination (page numbers)
  - Game levels
  - Timed intervals
  - Batch processing
- **Common Operations**:
  ```python
  # Creating and using ranges
  numbers = range(1, 101)     # 1 to 100
  even_nums = range(0, 101, 2)  # Even numbers
  
  # Common patterns
  for page in range(1, total_pages + 1):
      process_page(page)
  
  # Converting to list when needed
  first_ten = list(range(1, 11))  # [1,2,3,4,5,6,7,8,9,10]
  ```

### Key Considerations for Complex Types

1. **Performance Characteristics**:
   - Lists: Good for ordered data with frequent modifications
   - Tuples: Best for immutable data, slightly more memory efficient
   - Dictionaries: Excellent for key-based lookups
   - Sets: Perfect for unique collections and membership testing
   - Range: Most memory efficient for number sequences

2. **When to Use Each**:
   - Use **lists** when order matters and items will change
   - Use **tuples** for fixed collections or dictionary keys
   - Use **dictionaries** when you need key-based access
   - Use **sets** when you need unique items or set operations
   - Use **range** for number sequences, especially in loops

3. **Memory Usage**:
   - Lists and dictionaries are more memory-intensive
   - Tuples and ranges are memory-efficient
   - Sets use hash tables (balanced between memory and speed)

For practical examples and exercises using these types, see the [Complex Data Types Document](../ComplexDataTypes-Operators-Conditions-Loops/MCL.Level1.CDT.md).

## 3. User-Defined Data Types

### Classes
- **What**: Custom data types defined by the programmer
- **Why Important**:
  - Create reusable blueprints for objects
  - Combine data and behavior
  - Organize code in an object-oriented way
- **Example**:
  ```python
  class Student:
      def __init__(self, name, grade):
          self.name = name
          self.grade = grade
      
      def is_passing(self):
          return self.grade >= 60
  
  # Using the class
  student1 = Student("Alice", 85)
  ```

### Custom Collections
- **What**: Custom data structures built from existing types
- **Why Important**:
  - Create specialized data structures
  - Optimize for specific use cases
  - Add custom functionality
- **Example**:
  ```python
  class UniqueList(list):
      def append(self, item):
          if item not in self:
              super().append(item)
  
  # Using the custom collection
  unique_items = UniqueList([1, 2, 3])
  ```

## Type Conversion
```python
# String to Integer
age_str = "25"
age_int = int(age_str)      # 25

# Integer to Float
count = 5
count_float = float(count)  # 5.0

# Float to String
price = 19.99
price_str = str(price)      # "19.99"

# String to List
text = "Hello"
char_list = list(text)      # ['H', 'e', 'l', 'l', 'o']
```

## Best Practices
1. Choose the appropriate data type for your needs
2. Consider memory usage and performance
3. Use type hints for better code readability
4. Convert between types only when necessary
5. Be aware of type-specific operations and methods

---
© 2025 MathCodeLab Team. All Rights Reserved.