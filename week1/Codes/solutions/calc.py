"""Lab 3 reference solution: numeric input and arithmetic output."""

# Assume numeric input and a nonzero second number.
first_text = input("First number: ")
second_text = input("Second number: ")
a = float(first_text)
b = float(second_text)

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")

# Tests (sum, difference, product, displayed quotient):
# 8, 2 -> 10.0, 6.0, 16.0, 4.00
# 7, 3 -> 10.0, 4.0, 21.0, 2.33
# 2.5, 0.5 -> 3.0, 2.0, 1.25, 5.00
# -6, 2 -> -4.0, -8.0, -12.0, -3.00
# Zero divisors and nonnumeric text are outside this lab's valid input.
