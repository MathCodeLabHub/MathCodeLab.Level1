<img src="../../../../CommonResources/Logo.MathCodeLab.Light.png#gh-light-mode-only" alt="MathCodeLab" width="200"/>
<img src="../../../../CommonResources/Logo.MathCodeLab.Dark.jpg#gh-dark-mode-only" alt="MathCodeLab" width="200"/>

# Look and Say Three Digits Number! 🔢➡️📝

Hey there, word wizard! Ready for an exciting challenge? We're going to convert any three-digit number (100-999) into words using only conditions and loops - no lists or functions allowed!

## The Challenge 🎯

Convert numbers like:
- 123 → "one hundred twenty three"
- 456 → "four hundred fifty six"
- 789 → "seven hundred eighty nine"

## What You'll Learn 📚

- How to break down numbers into hundreds, tens, and ones
- Using Python's modern `match` statement for cleaner conditionals
- Building strings piece by piece
- Problem-solving without helper functions or arrays
- Pattern matching with multiple cases

## Breaking Down the Problem 🧩

Every three-digit number has three parts:
- **Hundreds place**: 1-9 (like the "4" in 456)
- **Tens place**: 0-9 (like the "5" in 456) 
- **Ones place**: 0-9 (like the "6" in 456)

### Step 1: Extract Each Digit
```python
# Let's say we have the number 456
number = 456

# Extract hundreds digit (4)
hundreds = number // 100  # Integer division gives us 4

# Extract tens digit (5)
tens = (number // 10) % 10  # Get tens place

# Extract ones digit (6)
ones = number % 10  # Remainder gives us ones place

print(f"Hundreds: {hundreds}, Tens: {tens}, Ones: {ones}")
```

### Step 2: Convert Digits to Words
Now we need to convert each digit to its word form. Since we can't use lists, we'll use Python's modern `match` statement!

#### What is Match Statement? 🆕
The `match` statement (introduced in Python 3.10) is a cleaner way to handle multiple conditions. Instead of long `if/elif` chains, we can use pattern matching:

```python
# Old way with if/elif
if number == 1:
    word = "one"
elif number == 2:
    word = "two"
# ... many more elif statements

# New way with match
match number:
    case 1:
        word = "one"
    case 2:
        word = "two"
    # ... much cleaner!
```

```python
# Convert hundreds digit to word using match statement
hundreds_word = ""
match hundreds:
    case 1:
        hundreds_word = "one"
    case 2:
        hundreds_word = "two"
    case 3:
        hundreds_word = "three"
    case 4:
        hundreds_word = "four"
    case 5:
        hundreds_word = "five"
    case 6:
        hundreds_word = "six"
    case 7:
        hundreds_word = "seven"
    case 8:
        hundreds_word = "eight"
    case 9:
        hundreds_word = "nine"

print(f"Hundreds word: {hundreds_word}")
```

### Step 3: Handle Special Cases for Tens
The tens place is tricky because we have special words for 10-19!

```python
# Handle tens digit using match statement
tens_word = ""
ones_word = ""

match tens:
    case 1:
        # Special case for 10-19
        match ones:
            case 0:
                tens_word = "ten"
            case 1:
                tens_word = "eleven"
            case 2:
                tens_word = "twelve"
            case 3:
                tens_word = "thirteen"
            case 4:
                tens_word = "fourteen"
            case 5:
                tens_word = "fifteen"
            case 6:
                tens_word = "sixteen"
            case 7:
                tens_word = "seventeen"
            case 8:
                tens_word = "eighteen"
            case 9:
                tens_word = "nineteen"
        # For 10-19, we don't need a separate ones word
    case _:
        # Handle 20, 30, 40, etc.
        match tens:
            case 2:
                tens_word = "twenty"
            case 3:
                tens_word = "thirty"
            case 4:
                tens_word = "forty"
            case 5:
                tens_word = "fifty"
            case 6:
                tens_word = "sixty"
            case 7:
                tens_word = "seventy"
            case 8:
                tens_word = "eighty"
            case 9:
                tens_word = "ninety"
        
        # Handle ones digit (only if tens is not 1)
        match ones:
            case 1:
                ones_word = "one"
            case 2:
                ones_word = "two"
            case 3:
                ones_word = "three"
            case 4:
                ones_word = "four"
            case 5:
                ones_word = "five"
            case 6:
                ones_word = "six"
            case 7:
                ones_word = "seven"
            case 8:
                ones_word = "eight"
            case 9:
                ones_word = "nine"
```

## Complete Solution 🎉

Here's a complete working example:

```python
# Get input from user
number = int(input("Enter a three-digit number (100-999): "))

# Validate input
if number < 100 or number > 999:
    print("Please enter a number between 100 and 999!")
else:
    # Extract digits
    hundreds = number // 100
    tens = (number // 10) % 10
    ones = number % 10
    
    # Start building our result
    result = ""
    
    # Convert hundreds using match statement
    hundreds_word = ""
    match hundreds:
        case 1:
            hundreds_word = "one"
        case 2:
            hundreds_word = "two"
        case 3:
            hundreds_word = "three"
        case 4:
            hundreds_word = "four"
        case 5:
            hundreds_word = "five"
        case 6:
            hundreds_word = "six"
        case 7:
            hundreds_word = "seven"
        case 8:
            hundreds_word = "eight"
        case 9:
            hundreds_word = "nine"
    
    result = hundreds_word + " hundred"
    
    # Handle tens and ones using match statement
    match tens:
        case 1:
            # Special case for 10-19
            match ones:
                case 0:
                    result = result + " ten"
                case 1:
                    result = result + " eleven"
                case 2:
                    result = result + " twelve"
                case 3:
                    result = result + " thirteen"
                case 4:
                    result = result + " fourteen"
                case 5:
                    result = result + " fifteen"
                case 6:
                    result = result + " sixteen"
                case 7:
                    result = result + " seventeen"
                case 8:
                    result = result + " eighteen"
                case 9:
                    result = result + " nineteen"
        case _:
            # Handle tens (20, 30, 40, etc.)
            tens_word = ""
            match tens:
                case 2:
                    tens_word = "twenty"
                case 3:
                    tens_word = "thirty"
                case 4:
                    tens_word = "forty"
                case 5:
                    tens_word = "fifty"
                case 6:
                    tens_word = "sixty"
                case 7:
                    tens_word = "seventy"
                case 8:
                    tens_word = "eighty"
                case 9:
                    tens_word = "ninety"
            
            if tens_word != "":
                result = result + " " + tens_word
            
            # Handle ones
            ones_word = ""
            match ones:
                case 1:
                    ones_word = "one"
                case 2:
                    ones_word = "two"
                case 3:
                    ones_word = "three"
                case 4:
                    ones_word = "four"
                case 5:
                    ones_word = "five"
                case 6:
                    ones_word = "six"
                case 7:
                    ones_word = "seven"
                case 8:
                    ones_word = "eight"
                case 9:
                    ones_word = "nine"
            
            if ones_word != "":
                result = result + " " + ones_word
    
    print(f"{number} in words: {result}")
```

## Test Your Solution 🧪

Try these test cases:
- 123 → "one hundred twenty three"
- 456 → "four hundred fifty six"
- 789 → "seven hundred eighty nine"
- 100 → "one hundred"
- 205 → "two hundred five"
- 310 → "three hundred ten"
- 415 → "four hundred fifteen"
- 999 → "nine hundred ninety nine"

## Fun Challenges 🌟

1. **Add Validation**: Make sure the input is exactly 3 digits
2. **Handle Zero**: What happens with numbers like 101 or 405?
3. **Add Proper Formatting**: Make sure spacing looks perfect
4. **Create a Loop**: Let the user convert multiple numbers

## What Makes This Special? ✨

- **No Functions**: We solved this using only basic programming constructs
- **No Arrays/Lists**: Everything is done with conditions and variables
- **Problem Decomposition**: We broke a complex problem into simple steps
- **Pattern Recognition**: We identified patterns in number-to-word conversion

## Extended Challenge 🚀

Can you modify this to work with:
- Two-digit numbers (10-99)?
- Four-digit numbers (1000-9999)?
- What about handling the word "and" (like "one hundred and twenty three")?

Remember, the goal is to understand how computers process and convert data step by step. This puzzle teaches you to think algorithmically and break down complex problems into manageable pieces!

Happy coding! 🎊
