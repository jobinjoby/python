attendance = [18, 20, 19, 15, 21]

full_days = 0
total = 0

for students in attendance:
    if students >= 20:
        print("Full")
        full_days = full_days + 1
    else:
        print("Not Full")

    total = total + students

print("Full days:", full_days)
print("Total attendance:", total)
