#employee attendance tracker system
# Sample Input/Data (attendance.txt)

# --------------------------------------------------
# Employee Attendance Monitoring System
# --------------------------------------------------

# Function to read attendance records from file
def read_attendance():

    employees = []

    with open("attendance.txt", "r") as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            data = [field.strip() for field in line.split(",")]

            if len(data) < 2:
                continue

            employees.append(data)

    return employees


# --------------------------------------------------
# Task 1
# Count Present and Absent Employees
# --------------------------------------------------

def count_attendance():

    employees = read_attendance()

    present = 0
    absent = 0

    for emp in employees:

        if emp[1] == "P":

            present += 1

        else:

            absent += 1

    print("\nPresent Employees:", present)
    print("Absent Employees:", absent)


# --------------------------------------------------
# Task 2
# Display Absent Employee IDs
# --------------------------------------------------

def display_absent_employees():

    employees = read_attendance()

    print("\nAbsent Employee IDs:")

    for emp in employees:

        if emp[1] == "A":

            print(emp[0])


# --------------------------------------------------
# Task 3
# Calculate Attendance Percentage
# --------------------------------------------------

def attendance_percentage():

    employees = read_attendance()

    present = 0

    for emp in employees:

        if emp[1] == "P":

            present += 1

    total = len(employees)

    percentage = (present / total) * 100

    print("\nAttendance Percentage:", percentage, "%")


# --------------------------------------------------
# Task 4
# Generate Absentee Report
# --------------------------------------------------

def generate_absent_report():

    employees = read_attendance()

    file = open("absent_report.txt", "w")

    for emp in employees:

        if emp[1] == "A":

            file.write(emp[0] + "\n")

    file.close()

    print("\nAbsentee Report Generated Successfully")


# --------------------------------------------------
# Task 5
# Attendance Award Eligibility
# (Only if all employees are present)
# --------------------------------------------------

def attendance_award():

    employees = read_attendance()

    all_present = True

    for emp in employees:

        if emp[1] == "A":

            all_present = False

            break

    print("\nAttendance Award Eligibility:")

    if all_present == True:

        print("Eligible")

    else:

        print("Not Applicable")


# --------------------------------------------------
# Main Menu
# --------------------------------------------------

while True:

    print("\n")
    print("===== Employee Attendance Monitoring System =====")
    print("1. Count Present and Absent Employees")
    print("2. Display Absent Employee IDs")
    print("3. Calculate Attendance Percentage")
    print("4. Generate Absentee Report")
    print("5. Check Attendance Award Eligibility")
    print("6. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:

        count_attendance()

    elif choice == 2:

        display_absent_employees()

    elif choice == 3:

        attendance_percentage()

    elif choice == 4:

        generate_absent_report()

    elif choice == 5:

        attendance_award()

    elif choice == 6:

        print("Thank You")
        break

    else:

        print("Invalid Choice")


