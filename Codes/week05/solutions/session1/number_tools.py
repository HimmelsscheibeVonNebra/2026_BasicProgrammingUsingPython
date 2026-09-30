"""Lab 1 solution module: small statistics tools for lists of numbers."""


def average(numbers):
    return sum(numbers) / len(numbers)


def count_above(numbers, limit):
    count = 0
    for value in numbers:
        if value > limit:
            count += 1
    return count


if __name__ == "__main__":
    demo = [2, 4, 6, 8]
    print("Demo average:", average(demo))
