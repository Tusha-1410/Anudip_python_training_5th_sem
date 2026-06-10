# --------------------------------------------------
# Employee Payroll Management System
# --------------------------------------------------

# Function to read employee data from file

def read_employees():

    file = open("employees.txt", "r")

    employees = []

    for line in file:

        line = line.strip()

        data = line.split(",")

        employees.append(data)

    file.close()

    return employees


# --------------------------------------------------
# Function 1 : Display all employees

def display_employees():

    employees = read_employees()

    print("\nEmployee Records")

    for emp in employees:

        print("ID:", emp[0],
              "| Name:", emp[1],
              "| Salary:", emp[2])


# --------------------------------------------------
# Function 2 : Search Employee by ID

def search_employee():

    emp_id = input("Enter Employee ID: ")

    employees = read_employees()

    found = False

    for emp in employees:

        if emp[0] == emp_id:

            print("\nEmployee Found")
            print("ID:", emp[0])
            print("Name:", emp[1])
            print("Salary:", emp[2])

            found = True
            break

    if found == False:
        print("Employee Not Found")


# --------------------------------------------------
# Function 3 : Calculate Average Salary

def average_salary():

    employees = read_employees()

    total = 0

    for emp in employees:

        total += int(emp[2])

    avg = total / len(employees)

    print("\nAverage Salary =", round(avg, 2))


# --------------------------------------------------
# Function 4 : Highest and Lowest Salary

def highest_lowest_salary():

    employees = read_employees()

    highest = employees[0]
    lowest = employees[0]

    for emp in employees:

        if int(emp[2]) > int(highest[2]):
            highest = emp

        if int(emp[2]) < int(lowest[2]):
            lowest = emp

    print("\nHighest Paid Employee")
    print(highest[1], "-", highest[2])

    print("\nLowest Paid Employee")
    print(lowest[1], "-", lowest[2])


# --------------------------------------------------
# Function 5 : Employees earning above 50000

def employees_above_50000():

    employees = read_employees()

    print("\nEmployees Earning Above 50000")

    for emp in employees:

        if int(emp[2]) > 50000:

            print(emp[0], emp[1], emp[2])


# --------------------------------------------------
# Function 6 : Add New Employee

def add_employee():

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    salary = input("Enter Salary: ")

    file = open("employees.txt", "a")

    file.write("\n" + emp_id + "," + name + "," + salary)

    file.close()

    print("Employee Added Successfully")


# --------------------------------------------------
# Function 7 : Salary Categories

def salary_categories():

    employees = read_employees()

    print("\nSalary Categories")

    for emp in employees:

        salary = int(emp[2])

        if salary >= 60000:

            category = "High"

        elif salary >= 40000:

            category = "Medium"

        else:

            category = "Low"

        print(emp[1], "->", category)


# --------------------------------------------------
# Main Menu

while True:

    print("\n")
    print("===== Employee Payroll System =====")
    print("1. Display All Employees")
    print("2. Search Employee")
    print("3. Average Salary")
    print("4. Highest and Lowest Paid Employee")
    print("5. Employees Above 50000")
    print("6. Add New Employee")
    print("7. Salary Categories")
    print("8. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_employees()

    elif choice == 2:
        search_employee()

    elif choice == 3:
        average_salary()

    elif choice == 4:
        highest_lowest_salary()

    elif choice == 5:
        employees_above_50000()

    elif choice == 6:
        add_employee()

    elif choice == 7:
        salary_categories()

    elif choice == 8:
        print("Thank You")
        break

    else:
        print("Invalid Choice")
        