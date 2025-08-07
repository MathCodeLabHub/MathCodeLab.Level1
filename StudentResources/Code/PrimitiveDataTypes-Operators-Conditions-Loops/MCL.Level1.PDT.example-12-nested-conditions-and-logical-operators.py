# Example 12: Nested conditions and logical operators
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
