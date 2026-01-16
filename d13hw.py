filename = "students.txt"

try:
    with open(filename, "r") as file:
        content = file.read()
        if content:
            print("Existing student names:")
            print(content)
        else:
            print("The file exists but is empty.")
except FileNotFoundError:
    print("No existing file found. A new one will be created.")

try:
    n = int(input("How many student names do you want to add? "))
except ValueError:
    print("Invalid number.")
    exit()

with open(filename, "a") as file:
    for i in range(n):
        name = input(f"Enter name {i + 1}: ").strip()
        if name:
            file.write(name + "\n")

print("\nUpdated list of student names:")
with open(filename, "r") as file:
    print(file.read())
10
1