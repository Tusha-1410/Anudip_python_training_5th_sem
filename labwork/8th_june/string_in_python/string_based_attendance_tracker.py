# String-Based Attendance Tracker

# Attendance record
attendance = "PPAPPPAAPPPPAPP"

# ----------------------------------
# Task 1: Count Present and Absent Days

present_days = attendance.count("P")
absent_days = attendance.count("A")

print("Present Days:", present_days)
print("Absent Days:", absent_days)

# ----------------------------------
# Task 2: Calculate Attendance Percentage

total_days = len(attendance)

attendance_percentage = (present_days / total_days) * 100

print("\nAttendance Percentage:", attendance_percentage, "%")

# ----------------------------------
# Task 3: Find Longest Consecutive Present Streak

current_present = 0
longest_present = 0

for ch in attendance:

    if ch == "P":
        current_present += 1

        if current_present > longest_present:
            longest_present = current_present

    else:
        current_present = 0

print("\nLongest Present Streak:", longest_present)

# ----------------------------------
# Task 4: Find Longest Consecutive Absent Streak

current_absent = 0
longest_absent = 0

for ch in attendance:

    if ch == "A":
        current_absent += 1

        if current_absent > longest_absent:
            longest_absent = current_absent

    else:
        current_absent = 0

print("Longest Absent Streak:", longest_absent)

# ----------------------------------
# Task 5: Check Attendance Status

if attendance_percentage < 75:
    print("\nAttendance Status: Below 75%")
else:
    print("\nAttendance Status: Above 75%")
    