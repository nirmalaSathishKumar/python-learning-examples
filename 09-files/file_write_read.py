with open("sample.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Python file handling.\n")
    file.write("Writing to files is easy.\n")

print("File written successfully")

with open("sample.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)
