with open("lines.txt", "w") as file:
    lines = ["First line\n", "Second line\n", "Third line\n"]
    file.writelines(lines)

print("Reading line by line:")
with open("lines.txt", "r") as file:
    for line in file:
        print(line.strip())

print("\nReading all lines:")
with open("lines.txt", "r") as file:
    all_lines = file.readlines()
    print(all_lines)
