"""Lab 1 reference solution: string manipulation."""

text = input("Text: ").strip()

print(f"Length: {len(text)}")
print(f"Upper: {text.upper()}")
print(f"Reverse: {text[::-1]}")

if text:
    print(f"First: {text[0]}")
else:
    print("No text entered")

# Tests:
# "  Python  " -> Length: 6, Upper: PYTHON, Reverse: nohtyP, First: P
# " A " -> Length: 1, Upper: A, Reverse: A, First: A
# "   " -> Length: 0, empty Upper/Reverse, No text entered
