# Student Performance Analytics System

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

# 1. Display All Student Records

print("ALL STUDENT RECORDS")

for sid in students:
    print(sid,
          students[sid]["name"],
          students[sid]["marks"])

# 2. Search Student

search_id = input("\nEnter Student ID: ")

if search_id in students:
    print("Student Found")
    print("Name :", students[search_id]["name"])
    print("Marks :", students[search_id]["marks"])
else:
    print("Student Not Found")

# 3. Add New Student

new_id = input("\nEnter New Student ID: ")
new_name = input("Enter Name: ")
new_marks = int(input("Enter Marks: "))

students[new_id] = {
    "name": new_name,
    "marks": new_marks
}

print("Student Added Successfully")

# 4. Update Marks

update_id = input("\nEnter Student ID: ")

if update_id in students:
    marks = int(input("Enter New Marks: "))
    students[update_id]["marks"] = marks
    print("Marks Updated")
else:
    print("Student Not Found")

# 5. Delete Student

delete_id = input("\nEnter Student ID: ")

if delete_id in students:
    del students[delete_id]
    print("Student Deleted")
else:
    print("Student Not Found")

# 6. Topper and Lowest Scorer

first = True

for sid in students:

    if first:
        topper_id = sid
        lowest_id = sid
        first = False

    if students[sid]["marks"] > students[topper_id]["marks"]:
        topper_id = sid

    if students[sid]["marks"] < students[lowest_id]["marks"]:
        lowest_id = sid

print("\nTOPPER")
print(topper_id,
      students[topper_id]["name"],
      students[topper_id]["marks"])

print("\nLOWEST SCORER")
print(lowest_id,
      students[lowest_id]["name"],
      students[lowest_id]["marks"])

# 7. Calculate Average

total_marks = 0

for sid in students:
    total_marks += students[sid]["marks"]

average = total_marks / len(students)

print("\nClass Average =", round(average, 2))

# 8. Pass and Fail Count

pass_count = 0
fail_count = 0

for sid in students:

    if students[sid]["marks"] >= 50:
        pass_count += 1
    else:
        fail_count += 1

print("\nPass Students =", pass_count)
print("Fail Students =", fail_count)

# 9. Generate Grades

print("\nSTUDENT GRADES")

for sid in students:

    marks = students[sid]["marks"]

    if marks >= 90:
        grade = "A"

    elif marks >= 75:
        grade = "B"

    elif marks >= 50:
        grade = "C"

    else:
        grade = "F"

    print(sid,
          students[sid]["name"],
          grade)

# 10. Students Above Average

print("\nSTUDENTS ABOVE AVERAGE")

for sid in students:

    if students[sid]["marks"] > average:
        print(sid,
              students[sid]["name"],
              students[sid]["marks"])

# 11. Top 5 Performers

print("\nTOP 5 PERFORMERS")

temp = students.copy()

for i in range(5):

    first = True

    for sid in temp:

        if first:
            top_id = sid
            first = False

        elif temp[sid]["marks"] > temp[top_id]["marks"]:
            top_id = sid

    print(i + 1,
          temp[top_id]["name"],
          temp[top_id]["marks"])

    del temp[top_id]

# 12. Scholarship Students

scholarship_students = {}

for sid in students:

    if students[sid]["marks"] > 85:
        scholarship_students[sid] = students[sid]

print("\nSCHOLARSHIP STUDENTS")

for sid in scholarship_students:
    print(sid,
          scholarship_students[sid]["name"],
          scholarship_students[sid]["marks"])
    