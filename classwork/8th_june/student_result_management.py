# Student Result Management System

# Dictionary containing student names and marks
student_marks = {
    "Anuj": 85,
    "Rahul": 72,
    "Priya": 91,
    "Neha": 68,
    "Amit": 78
}

# ----------------------------------
# Task 1: Display the marks of Priya

print("Marks of Priya:", student_marks["Priya"])

# ----------------------------------
# Task 2: Display the marks of Amit

print("Marks of Amit:", student_marks["Amit"])

# ----------------------------------
# Task 3: Update Rahul's marks from 72 to 80

student_marks["Rahul"] = 80

print("\nUpdated Marks of Rahul:", student_marks["Rahul"])

# ----------------------------------
# Task 4: Check whether Rohan exists

if "Rohan" in student_marks:
    print("\nRohan Exists")
else:
    print("\nRohan Does Not Exist")

# ----------------------------------
# Task 5: Display all student names

print("\nStudent Names:")

for student in student_marks:
    print(student)

# ----------------------------------
# Task 6: Display all marks

print("\nStudent Marks:")

for student in student_marks:
    print(student_marks[student])

# ----------------------------------
# Task 7: Find the highest scorer

highest_student = ""
highest_marks = 0

for student in student_marks:
    if student_marks[student] > highest_marks:
        highest_marks = student_marks[student]
        highest_student = student

print("\nHighest Scorer:")
print(highest_student, "-", highest_marks)

# ----------------------------------
# Task 8: Add a new student

student_marks["Rohan"] = 88

print("\nRohan Added Successfully")

# ----------------------------------
# Task 9: Remove a student

del student_marks["Neha"]

print("Neha Removed Successfully")

# ----------------------------------
# Task 10: Display all student records

print("\nFinal Student Records:")

for student in student_marks:
    print(student, ":", student_marks[student])
    