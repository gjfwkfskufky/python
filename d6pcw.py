attendance = [18, 20, 19, 15, 21]

total_attendance = 0
full_days = 0

for students in attendance:
    total_attendance += students

    if students >= 20:
        print("Full")
        full_days += 1
    else:
        print("Not Full")

print("\nTotal attendance:", total_attendance)
print("Number of full days:", full_days)
