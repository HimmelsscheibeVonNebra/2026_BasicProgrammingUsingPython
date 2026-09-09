"""Lab 4 reference solution: height conversion and BMI arithmetic."""

# Assume positive numeric measurements. This exercise does not classify health.
height_cm = float(input("Height (cm): "))
weight_kg = float(input("Weight (kg): "))

height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)

print(f"Height: {height_m:.2f} m")
print(f"Weight: {weight_kg:.1f} kg")
print(f"Your BMI is {bmi:.1f}")

# Tests (height in cm, weight in kg -> displayed height and BMI):
# 175, 70 -> 1.75 m, BMI 22.9
# 160, 64 -> 1.60 m, BMI 25.0
# 180, 81 -> 1.80 m, BMI 25.0
# Zero height and nonnumeric text are outside this lab's valid input.
