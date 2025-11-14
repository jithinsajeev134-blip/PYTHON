attendance = [18, 20, 19, 15, 21]

full_days = 0
total_attendance = 0

for std in attendance:
    if std >= 20:
        print("Full")
        
        full_days += 1
    else:
        print("Not Full")
    
    total_attendance += std

print(full_days)
print(total_attendance)
