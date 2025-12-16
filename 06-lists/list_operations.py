numbers = [5, 2, 8, 1, 9]

numbers.sort()
print(f"Sorted ascending: {numbers}")

numbers.sort(reverse=True)
print(f"Sorted descending: {numbers}")

numbers.reverse()
print(f"Reversed: {numbers}")

print(f"Max: {max(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Sum: {sum(numbers)}")
