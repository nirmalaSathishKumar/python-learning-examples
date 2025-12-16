person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(f"Person: {person}")
print(f"Name: {person['name']}")
print(f"Age: {person.get('age')}")

person["email"] = "alice@example.com"
print(f"After adding email: {person}")

person["age"] = 31
print(f"After update: {person}")

del person["city"]
print(f"After deletion: {person}")
