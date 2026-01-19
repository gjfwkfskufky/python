import random
import math

names_input = input("Enter customer names (comma-separated): ")

names = [name.strip() for name in names_input.split(",")]

unique_names = list(set(names))

random.shuffle(unique_names)

winners = random.sample(unique_names, 2)

reversed_winners = [winner[::-1] for winner in winners]

print("Lucky Draw Winners:")
for winner in reversed_winners:
    print(winner)

total_participants = len(unique_names)
print("Total unique participants:", total_participants)

sqrt_participants = round(math.sqrt(total_participants))
print("Square root of participants (rounded):", sqrt_participants)
