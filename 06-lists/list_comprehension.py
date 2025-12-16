numbers = [1, 2, 3, 4, 5]

squares = [x**2 for x in numbers]
print(f"Squares: {squares}")

evens = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {evens}")

doubled_evens = [x*2 for x in numbers if x % 2 == 0]
print(f"Doubled evens: {doubled_evens}")
