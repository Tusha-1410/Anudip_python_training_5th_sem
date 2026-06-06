# Employee Salary Processing

# Each employee record contains:
# Employee Name and Salary

employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

# ----------------------------------------
# Task 1: Display Employees Earning Above ₹50,000

print("Employees Earning Above ₹50,000:")

for employee in employees:

    # employee[1] contains salary
    if employee[1] > 50000:
        print(employee[0], "₹", employee[1])

print("-" * 40)

# ----------------------------------------
# Task 2: Find the Highest-Paid Employee

# Assume first employee has the highest salary
highest_paid = employees[0]

# Compare each employee's salary with current highest salary
for employee in employees:

    if employee[1] > highest_paid[1]:
        highest_paid = employee

print("Highest-Paid Employee:")
print(highest_paid[0], "₹", highest_paid[1])

print("-" * 40)

# ----------------------------------------
# Task 3: Calculate Total Salary Expenditure

total_salary = 0

# Add salaries of all employees
for employee in employees:
    total_salary += employee[1]

print("Total Salary Expenditure: ₹", total_salary)

print("-" * 40)

# ----------------------------------------
# Task 4: Count Employees Earning Below ₹40,000

count = 0

for employee in employees:

    if employee[1] < 40000:
        count += 1

print("Employees Earning Below ₹40,000:", count)

print("-" * 40)
