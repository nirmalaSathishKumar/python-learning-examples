grades = {"Alice": 90, "Bob": 85, "Charlie": 92}

for name in grades:
    print(f"{name}: {grades[name]}")

print()

for name, grade in grades.items():
    print(f"{name} scored {grade}")

print()

print(f"Keys: {list(grades.keys())}")
print(f"Values: {list(grades.values())}")
