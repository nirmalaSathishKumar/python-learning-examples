import json

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "coding", "hiking"]
}

json_string = json.dumps(person, indent=2)
print("JSON string:")
print(json_string)

print("\nParsing back to Python:")
parsed_data = json.loads(json_string)
print(f"Name: {parsed_data['name']}")
print(f"Hobbies: {parsed_data['hobbies']}")
