# Employee Salary Processing

# Dictionary containing employee IDs and their salaries
salary = {
    "EMP101": 45000,
    "EMP102": 62000,
    "EMP103": 38000,
    "EMP104": 75000,
    "EMP105": 54000,
    "EMP106": 29000,
    "EMP107": 82000,
    "EMP108": 48000,
    "EMP109": 36000,
    "EMP110": 68000
}

# ----------------------------------
# Task 1: Display employees earning above ₹60,000

print("Employees earning above ₹60,000:")

for emp in salary:
    if salary[emp] > 60000:
        print(emp, "-", salary[emp])

# ----------------------------------
# Task 2: Count employees earning below ₹40,000

count = 0

for emp in salary:
    if salary[emp] < 40000:
        count += 1

print("\nEmployees earning below ₹40,000:", count)

# ----------------------------------
# Task 3: Find the highest-paid employee

highest_emp = ""
highest_salary = 0

for emp in salary:
    if salary[emp] > highest_salary:
        highest_salary = salary[emp]
        highest_emp = emp

print("\nHighest-Paid Employee:")
print(highest_emp, "-", highest_salary)

# ----------------------------------
# Task 4: Create a list of employees eligible for bonus

bonus_list = []

for emp in salary:
    if salary[emp] > 50000:
        bonus_list.append(emp)

print("\nEmployees Eligible for Bonus:")
print(bonus_list)

# ----------------------------------
# Task 5: Calculate the average salary

total_salary = 0

for emp in salary:
    total_salary += salary[emp]

average_salary = total_salary / len(salary)

print("\nAverage Salary:", average_salary)
