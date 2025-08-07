# Example 15: Else clause on a for loop
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
