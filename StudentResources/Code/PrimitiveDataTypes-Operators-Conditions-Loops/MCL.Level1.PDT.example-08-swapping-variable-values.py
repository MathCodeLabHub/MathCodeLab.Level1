# Example 8: Swapping variable values
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
