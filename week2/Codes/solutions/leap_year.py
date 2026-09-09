"""Lab 4 reference solution: the Gregorian leap-year rule."""

# Assume integer-formatted input. Range validation follows conversion.
year = int(input("Year: "))

if year <= 0:
    print("Enter a positive year")
else:
    is_leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
    if is_leap:
        print(f"{year}: Leap year")
    else:
        print(f"{year}: Not a leap year")

# Tests:
# 2024, 2000 -> <year>: Leap year
# 2023, 1900 -> <year>: Not a leap year
# 0, -4 -> Enter a positive year
