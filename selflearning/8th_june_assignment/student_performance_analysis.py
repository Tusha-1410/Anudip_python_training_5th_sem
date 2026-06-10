# Student Performance Analytics System

# Dictionary storing details of 30 students
students = {
    "S101": {"name": "Anuj", "marks": 85},
    "S102": {"name": "Rahul", "marks": 72},
    "S103": {"name": "Priya", "marks": 91},
    "S104": {"name": "Neha", "marks": 48},
    "S105": {"name": "Aman", "marks": 67},
    "S106": {"name": "Riya", "marks": 95},
    "S107": {"name": "Karan", "marks": 54},
    "S108": {"name": "Sneha", "marks": 88},
    "S109": {"name": "Vikas", "marks": 39},
    "S110": {"name": "Pooja", "marks": 77},
    "S111": {"name": "Arjun", "marks": 82},
    "S112": {"name": "Nikita", "marks": 93},
    "S113": {"name": "Rohit", "marks": 58},
    "S114": {"name": "Meena", "marks": 45},
    "S115": {"name": "Sahil", "marks": 70},
    "S116": {"name": "Deepak", "marks": 99},
    "S117": {"name": "Tina", "marks": 62},
    "S118": {"name": "Mohit", "marks": 84},
    "S119": {"name": "Simran", "marks": 90},
    "S120": {"name": "Yash", "marks": 41},
    "S121": {"name": "Kriti", "marks": 76},
    "S122": {"name": "Harsh", "marks": 68},
    "S123": {"name": "Isha", "marks": 97},
    "S124": {"name": "Rakesh", "marks": 35},
    "S125": {"name": "Aarti", "marks": 81},
    "S126": {"name": "Nitin", "marks": 74},
    "S127": {"name": "Payal", "marks": 87},
    "S128": {"name": "Manoj", "marks": 52},
    "S129": {"name": "Komal", "marks": 66},
    "S130": {"name": "Varun", "marks": 92}
}

# ---------------------------------------------------
# 1. Display all student records
print("ALL STUDENT RECORDS")
for sid, details in students.items():
    print(sid, ":", details)

# ---------------------------------------------------
# 2. Search a student using Student ID
search_id = input("\nEnter Student ID to Search: ")

if search_id in students:
    print("Student Found:", students[search_id])
else:
    print("Student Not Found")

# ---------------------------------------------------
# 3. Add a new student
new_id = input("\nEnter New Student ID: ")
new_name = input("Enter Student Name: ")
new_marks = int(input("Enter Marks: "))

students[new_id] = {"name": new_name, "marks": new_marks}
print("Student Added Successfully!")

# ---------------------------------------------------
# 4. Update marks of an existing student
update_id = input("\nEnter Student ID to Update Marks: ")

if update_id in students:
    new_marks = int(input("Enter New Marks: "))
    students[update_id]["marks"] = new_marks
    print("Marks Updated Successfully!")
else:
    print("Student Not Found")

# ---------------------------------------------------
# 5. Delete a student
delete_id = input("\nEnter Student ID to Delete: ")

if delete_id in students:
    del students[delete_id]
    print("Student Deleted Successfully!")
else:
    print("Student Not Found")

# ---------------------------------------------------
# 6. Find Topper and Lowest Scorer

topper_id = max(students, key=lambda x: students[x]["marks"])
lowest_id = min(students, key=lambda x: students[x]["marks"])

print("\nTOPPER")
print(topper_id, students[topper_id])

print("\nLOWEST SCORER")
print(lowest_id, students[lowest_id])

# ---------------------------------------------------
# 7. Calculate Class Average

total_marks = 0

for details in students.values():
    total_marks += details["marks"]

average = total_marks / len(students)

print("\nClass Average =", round(average, 2))

# ---------------------------------------------------
# 8. Count Pass and Fail Students

pass_count = 0
fail_count = 0

for details in students.values():
    if details["marks"] >= 50:
        pass_count += 1
    else:
        fail_count += 1

print("\nPass Students =", pass_count)
print("Fail Students =", fail_count)

# ---------------------------------------------------
# 9. Generate Grades

print("\nSTUDENT GRADES")

for sid, details in students.items():

    marks = details["marks"]

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "F"

    print(sid, "-", details["name"], ":", grade)

# ---------------------------------------------------
# 10. Display Students Scoring Above Average

print("\nSTUDENTS SCORING ABOVE AVERAGE")

for sid, details in students.items():
    if details["marks"] > average:
        print(sid, "-", details["name"], "-", details["marks"])

# ---------------------------------------------------
# 11. Display Top 5 Performers

print("\nTOP 5 PERFORMERS")

sorted_students = sorted(
    students.items(),
    key=lambda x: x[1]["marks"],
    reverse=True
)

for sid, details in sorted_students[:5]:
    print(sid, "-", details["name"], "-", details["marks"])

# ---------------------------------------------------
# 12. Scholarship Students (Marks > 85)

scholarship_students = {}

for sid, details in students.items():
    if details["marks"] > 85:
        scholarship_students[sid] = details

print("\nSCHOLARSHIP STUDENTS")

for sid, details in scholarship_students.items():
    print(sid, ":", details)
