filename = "items.txt"

item = input("Enter the name of a new item: ").strip()

with open(filename, "a", encoding="utf-8") as file:
    file.write(item + "\n")

print("\nFull list of items:")
with open(filename, "r", encoding="utf-8") as file:
    for index, line in enumerate(file, start=1):
        print(f"{index}. {line.strip()}")
