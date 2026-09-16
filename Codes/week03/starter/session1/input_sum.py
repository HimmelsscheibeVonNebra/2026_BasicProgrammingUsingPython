"""Practice 2: sum integers until 0. Assume integer-formatted input.
Tests: 3,5,0 -> Total: 8; 0 -> Total: 0; -2,5,0 -> Total: 3.
"""
total = 0
while True:
    number = int(input("Integer (0: stop): "))
    if number == 0:
        break
    # TODO: add number to total.
print("Total:", total)
