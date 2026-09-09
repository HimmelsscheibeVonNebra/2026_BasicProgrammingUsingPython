"""Lab 2 reference solution: integer scores and grade thresholds."""

# Assume integer-formatted input. Range validation follows conversion.
score = int(input("Score: "))

if not 0 <= score <= 100:
    print("Invalid score")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# Tests:
# -1, 101 -> Invalid score
# 0, 59 -> F; 60, 69 -> D; 70, 79 -> C
# 80, 89 -> B; 90, 100 -> A
