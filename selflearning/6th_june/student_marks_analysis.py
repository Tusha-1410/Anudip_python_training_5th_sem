# Student Marks Analysis

marks = {
    "Aarav": 78,
    "Diya": 92,
    "Rohan": 45,
    "Ishita": 88,
    "Kabir": 56,
    "Meera": 39,
    "Arjun": 95,
    "Saanvi": 67,
    "Vivaan": 82,
    "Anaya": 51
}

# ----------------------------------
# Students scoring 80 or above

print("Students scoring 80 or above:")

for student in marks:
    if marks[student] >= 80:
        print(student, "-", marks[student])

# ----------------------------------
# Count failed students

fail_count = 0

for student in marks:
    if marks[student] < 40:
        fail_count += 1

print("\nFailed Students:", fail_count)

# ----------------------------------
# Find highest scorer

highest_student = ""
highest_marks = 0

for student in marks:
    if marks[student] > highest_marks:
        highest_marks = marks[student]
        highest_student = student

print("\nHighest Scorer:")
print(highest_student, "-", highest_marks)

# ----------------------------------
# Students scoring between 60 and 75

students_list = []

for student in marks:
    if marks[student] >= 60 and marks[student] <= 75:
        students_list.append(student)

print("\nStudents scoring between 60 and 75:")
print(students_list)

# ----------------------------------
# Assign Grades

print("\nGrades:")

for student in marks:

    score = marks[student]

    if score >= 90:
        grade = "A"

    elif score >= 75:
        grade = "B"

    elif score >= 50:
        grade = "C"

    else:
        grade = "F"

    print(student, "-", grade)
    