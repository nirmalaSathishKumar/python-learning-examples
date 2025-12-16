def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

def create_profile(name, age=18, city="Unknown"):
    return f"{name}, {age}, from {city}"

print(greet("Alice"))
print(greet("Bob", "Hi"))
print(create_profile("Charlie"))
print(create_profile("Diana", 25, "New York"))
