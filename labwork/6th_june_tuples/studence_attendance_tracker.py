# Student Attendance Tracker

# P = Present
# A = Absent

attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

# ----------------------------------------
# Task 1: Count Present and Absent Days

present = 0
absent = 0

for day in attendance:

    if day == 'P':
        present += 1
    else:
        absent += 1

print("Present Days :", present)
print("Absent Days  :", absent)

print("-" * 40)

# ----------------------------------------
# Task 2: Calculate Attendance Percentage

# Formula:
# (Present Days / Total Days) * 100

attendance_percentage = (present / len(attendance)) * 100

print("Attendance Percentage:", attendance_percentage, "%")

print("-" * 40)

# ----------------------------------------
# Task 3: Determine Eligibility

# Minimum 75% attendance required

if attendance_percentage >= 75:
    print("Eligible for Examination")
else:
    print("Not Eligible for Examination")

print("-" * 40)

# ----------------------------------------
# Task 4: Display Positions Where Student Was Absent

print("Absent on Days:")

for i in range(len(attendance)):

    if attendance[i] == 'A':
        print("Day", i + 1)

print("-" * 40)
