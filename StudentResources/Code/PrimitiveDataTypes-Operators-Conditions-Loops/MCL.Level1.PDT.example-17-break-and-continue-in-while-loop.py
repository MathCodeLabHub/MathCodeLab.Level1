# Example 17: Using break and continue in a while loop
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
