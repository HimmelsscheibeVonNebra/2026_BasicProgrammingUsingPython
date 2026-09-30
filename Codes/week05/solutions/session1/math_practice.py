"""Practice 1 solution: circle statistics and a hypotenuse."""
import math

radius = float(input("Radius: "))
print("Area:", round(math.pi * radius ** 2, 2))
print("Circumference:", round(2 * math.pi * radius, 2))

a = float(input("First leg: "))
b = float(input("Second leg: "))
print("Hypotenuse:", round(math.hypot(a, b), 2))
