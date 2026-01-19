import random
import math

names_input = input("Enter guest names (comma-separated): ")

names = [name.strip() for name in names_input.split(",")]
unique_names = list(set(names))

chosen_name = random.choice(unique_names)
reversed_name = chosen_name[::-1]

count = len(unique_names)
rounded_sqrt = round(math.sqrt(count))

print("Randomly chosen name:", chosen_name)
print("Reversed name:", reversed_name)
print("Total unique names:", count)
print("Rounded square root:", rounded_sqrt)
