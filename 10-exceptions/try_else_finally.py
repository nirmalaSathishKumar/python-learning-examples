try:
    numbers = [1, 2, 3]
    print(f"Element: {numbers[1]}")
except IndexError:
    print("Index out of range")
else:
    print("No exception occurred")
finally:
    print("This always executes")

print("\nSecond example:")
try:
    value = 10 / 2
    print(f"Value: {value}")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division successful")
finally:
    print("Cleanup complete")
