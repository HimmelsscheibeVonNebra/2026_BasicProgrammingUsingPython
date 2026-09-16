"""Lab 3: complete both parts. Assume integer-formatted input.
Tests: 2 -> 9 single-table equations; 9 -> last equation 9 x 9 = 81;
1 or 10 -> Invalid table. The all-tables section always has 72 equations.
"""
table = int(input("Table (2-9): "))
# TODO: validate table, then print factors 1 through 9.

print("All tables:")
for table in range(2, 10):
    for factor in range(1, 10):
        # TODO: print one equation.
        pass
    print()
