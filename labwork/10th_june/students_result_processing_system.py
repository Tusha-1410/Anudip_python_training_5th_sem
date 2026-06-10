# --------------------------------------------------
# Student Result Processing System
# --------------------------------------------------

# Function to read student records from file

def read_students():

    file = open("results.txt", "r")

    students = []

    for line in file:

        line = line.strip()

        data = line.split(",")

        students.append(data)

    file.close()

    return students


# --------------------------------------------------
# Function 1 : Display all students

def display_students():

    students = read_students()

    print("\nStudent Records")

    for student in students:

        print("ID:", student[0],
              "| Name:", student[1],
              "| Marks:", student[2])


# --------------------------------------------------
# Function 2 : Search student by ID

def search_student():

    student_id = input("Enter Student ID: ")

    students = read_students()

    found = False

    for student in students:

        if student[0] == student_id:

            print("\nStudent Found")
            print("ID:", student[0])
            print("Name:", student[1])
            print("Marks:", student[2])

            found = True
            break

    if found == False:
        print("Student Not Found")


# --------------------------------------------------
# Function 3 : Find Topper and Lowest Scorer

def topper_lowest():

    students = read_students()

    topper = students[0]
    lowest = students[0]

    for student in students:

        if int(student[2]) > int(topper[2]):
            topper = student

        if int(student[2]) < int(lowest[2]):
            lowest = student

    print("\nTopper")
    print(topper[1], "-", topper[2])

    print("\nLowest Scorer")
    print(lowest[1], "-", lowest[2])


# --------------------------------------------------
# Function 4 : Calculate Class Average

def class_average():

    students = read_students()

    total = 0

    for student in students:

        total += int(student[2])

    average = total / len(students)

    print("\nClass Average =", round(average, 2))


# --------------------------------------------------
# Function 5 : Count Pass and Fail Students

def pass_fail_count():

    students = read_students()

    passed = 0
    failed = 0

    for student in students:

        marks = int(student[2])

        if marks >= 40:
            passed += 1
        else:
            failed += 1

    print("\nPassed Students =", passed)
    print("Failed Students =", failed)


# --------------------------------------------------
# Function 6 : Generate Grades

def generate_grades():

    students = read_students()

    print("\nStudent Grades")

    for student in students:

        marks = int(student[2])

        if marks >= 90:
            grade = "A"

        elif marks >= 75:
            grade = "B"

        elif marks >= 40:
            grade = "C"

        else:
            grade = "F"

        print(student[1], "->", grade)


# --------------------------------------------------
# Function 7 : Write Grade Report to grades.txt

def write_grade_report():

    students = read_students()

    file = open("grades.txt", "w")

    for student in students:

        marks = int(student[2])

        if marks >= 90:
            grade = "A"

        elif marks >= 75:
            grade = "B"

        elif marks >= 40:
            grade = "C"

        else:
            grade = "F"

        line = student[0] + "," + student[1] + "," + grade

        file.write(line + "\n")

    file.close()

    print("Grade Report Generated Successfully")
    print("Data stored in grades.txt")


# --------------------------------------------------
# Main Menu

while True:

    print("\n")
    print("===== Student Result Processing System =====")
    print("1. Display All Students")
    print("2. Search Student")
    print("3. Topper and Lowest Scorer")
    print("4. Class Average")
    print("5. Pass and Fail Count")
    print("6. Generate Grades")
    print("7. Write Grade Report")
    print("8. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_students()

    elif choice == 2:
        search_student()

    elif choice == 3:
        topper_lowest()

    elif choice == 4:
        class_average()

    elif choice == 5:
        pass_fail_count()

    elif choice == 6:
        generate_grades()

    elif choice == 7:
        write_grade_report()

    elif choice == 8:
        print("Thank You")
        break

    else:
        print("Invalid Choice")
        