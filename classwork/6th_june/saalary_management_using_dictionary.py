# Employee Salary Management Using Dictionary

# Dictionary to store:
# Employee ID -> Salary
employees = {}

# ----------------------------------------
# Input records of 10 employees

for i in range(1, 11):

    # Input employee ID
    emp_id = int(input(f"Enter Employee ID {i}: "))

    # Input employee salary
    salary = int(input("Enter Salary: "))

    # Store employee ID as key and salary as value
    employees[emp_id] = salary

print("-" * 40)

# ----------------------------------------
# Find total employees having salary above 30000

count = 0

# Traverse the dictionary
for emp_id in employees:

    # Check if salary is greater than 30000
    if employees[emp_id] > 30000:
        count += 1

print("Total Employees Having Salary Above 30000 =", count)

print("-" * 40)

# ----------------------------------------
# Display employees whose salary is below 20000

print("Employees Having Salary Below 20000:")

# Traverse the dictionary
for emp_id in employees:

    # Check if salary is less than 20000
    if employees[emp_id] < 20000:

        print("Employee ID :", emp_id)
        print("Salary      :", employees[emp_id])
        print("-" * 20)

print("-" * 40)
