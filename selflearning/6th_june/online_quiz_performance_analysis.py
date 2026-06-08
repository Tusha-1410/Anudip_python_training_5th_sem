# Online Quiz Performance Analysis

# Dictionary containing student IDs and quiz scores
quiz_scores = {
    "S001": 18,
    "S002": 12,
    "S003": 9,
    "S004": 20,
    "S005": 14,
    "S006": 7,
    "S007": 16,
    "S008": 10,
    "S009": 19,
    "S010": 13
}

# ----------------------------------
# Task 1: Display students scoring 15 or above

print("Students Scoring 15 or Above:")

for student in quiz_scores:
    if quiz_scores[student] >= 15:
        print(student, "-", quiz_scores[student])

# ----------------------------------
# Task 2: Count students scoring below 10

count = 0

for student in quiz_scores:
    if quiz_scores[student] < 10:
        count += 1

print("\nStudents Scoring Below 10:", count)

# ----------------------------------
# Task 3: Find the top performer

top_student = ""
highest_score = 0

for student in quiz_scores:
    if quiz_scores[student] > highest_score:
        highest_score = quiz_scores[student]
        top_student = student

print("\nTop Performer:")
print(top_student, "-", highest_score)

# ----------------------------------
# Task 4: Create a list of students who passed

passed_students = []

for student in quiz_scores:
    if quiz_scores[student] >= 10:
        passed_students.append(student)

print("\nStudents Who Passed:")
print(passed_students)

# ----------------------------------
# Task 5: Calculate the class average

total_marks = 0

for student in quiz_scores:
    total_marks += quiz_scores[student]

average = total_marks / len(quiz_scores)

print("\nClass Average:", average)
