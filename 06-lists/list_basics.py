numbers = [1, 2, 3, 4, 5]

print(f"List: {numbers}")
print(f"First element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")
print(f"Slice: {numbers[1:4]}")

numbers.append(6)
print(f"After append: {numbers}")

numbers.insert(0, 0)
print(f"After insert: {numbers}")

numbers.remove(3)
print(f"After remove: {numbers}")

print(f"Length: {len(numbers)}")
