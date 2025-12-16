import json

data = {
    "users": [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25}
    ]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=2)

print("Data written to file")

with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print("\nLoaded data:")
    for user in loaded_data["users"]:
        print(f"{user['name']}: {user['age']}")
