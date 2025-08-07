# Example 4: Simple data types
text    = "Goodbye"
integer = 99
decimal = 1.618
complex_no = 1 + 2j
truth   = False
nothing = None

print("Example 4: Simple data types and their types")
for item in [text, integer, decimal, complex_no, truth, nothing]:
    print(item, "is of type", type(item))
