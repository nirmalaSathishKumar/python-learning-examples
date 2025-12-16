try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found")

try:
    with open("test.txt", "w") as file:
        file.write("Testing error handling\n")
    print("File created successfully")
except Exception as e:
    print(f"Error: {e}")
