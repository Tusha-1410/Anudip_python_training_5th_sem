# --------------------------------------------------
# School Report Card Generator
# --------------------------------------------------

# Function to read student records from file
def read_students():

    file = open("marks.txt", "r")

    students = []

    for line in file:

        line = line.strip()

        data = line.split(",")

        students.append(data)

    file.close()

    return students


# --------------------------------------------------
# Function to calculate grade
# --------------------------------------------------

def calculate_grade(marks):

    if marks >= 90:
        return "A+"

    elif marks >= 75:
        return "A"

    elif marks >= 60:
        return "B"

    elif marks >= 40:
        return "C"

    else:
        return "F"


# --------------------------------------------------
# Task 1 & 2
# Generate Report Card File
# --------------------------------------------------

def generate_report_card():

    students = read_students()

    file = open("report_card.txt", "w")

    for student in students:

        marks = int(student[2])

        grade = calculate_grade(marks)

        line = student[0] + "," + student[1] + "," + student[2] + "," + grade

        file.write(line + "\n")

    file.close()

    print("Report Card Generated Successfully")


# --------------------------------------------------
# Task 3
# Display Topper Details
# --------------------------------------------------

def display_topper():

    students = read_students()

    topper_name = ""
    highest_marks = 0

    for student in students:

        marks = int(student[2])

        if marks > highest_marks:

            highest_marks = marks

            topper_name = student[1]

    print("\nTopper Details")
    print("Topper:", topper_name, "(" + str(highest_marks) + ")")


# --------------------------------------------------
# Task 4
# Count Pass and Fail Students
# --------------------------------------------------

def count_pass_fail():

    students = read_students()

    passed = 0
    failed = 0

    for student in students:

        marks = int(student[2])

        if marks >= 40:

            passed += 1

        else:

            failed += 1

    print("\nStudent Result Summary")
    print("Passed Students:", passed)
    print("Failed Students:", failed)


# --------------------------------------------------
# Task 5
# Display Merit Certificate Students
# --------------------------------------------------

def merit_students():

    students = read_students()

    print("\nStudents Eligible For Merit Certificate")

    for student in students:

        marks = int(student[2])

        if marks >= 90:

            print(student[1], "-", marks)


# --------------------------------------------------
# Display All Students with Grades
# --------------------------------------------------

def display_report():

    students = read_students()

    print("\nStudent Report")

    for student in students:

        marks = int(student[2])

        grade = calculate_grade(marks)

        print("ID:", student[0],
              "| Name:", student[1],
              "| Marks:", marks,
              "| Grade:", grade)


# --------------------------------------------------
# Main Menu
# --------------------------------------------------

while True:

    print("\n")
    print("===== School Report Card Generator =====")
    print("1. Display Student Report")
    print("2. Generate Report Card File")
    print("3. Display Topper")
    print("4. Count Pass/Fail Students")
    print("5. Display Merit Students")
    print("6. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:

        display_report()

    elif choice == 2:

        generate_report_card()

    elif choice == 3:

        display_topper()

    elif choice == 4:

        count_pass_fail()

    elif choice == 5:

        merit_students()

    elif choice == 6:

        print("Thank You")
        break

    else:

        print("Invalid Choice")
        