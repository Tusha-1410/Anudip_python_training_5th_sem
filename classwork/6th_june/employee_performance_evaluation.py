# Employee Performance Evaluation Using Tuples

# Each employee record contains (Employee ID, Employee Name, Performance Score).
employees = (
    ("E101", "Anuj", 92),
    ("E102", "Rahul", 76),
    ("E103", "Priya", 58),
    ("E104", "Neha", 88),
    ("E105", "Amit", 45)
)

# ----------------------------------------
# Task 1: Display employees scoring 80 or above
# Loop through each employee and print details when score is at least 80.
print("Employees Scoring 80 or Above:")
for emp in employees:
    if emp[2] >= 80:
        print(emp[0], emp[1], emp[2])

print("-" * 40)

# ----------------------------------------
# Task 2: Count employees needing improvement
# Increment a counter for scores below 60.
count = 0
for emp in employees:
    if emp[2] < 60:
        count += 1

print("Employees Needing Improvement:", count)

print("-" * 40)

# ----------------------------------------
# Task 3: Find employee with highest score
# Start with the first record, then update when a higher score is found.
highest = employees[0]
for emp in employees:
    if emp[2] > highest[2]:
        highest = emp

print("Highest Performer:")
print(highest[0], highest[1], highest[2])

print("-" * 40)

# ----------------------------------------
# Task 4: Create list of employees scoring above 75
# Collect names of employees whose score is greater than 75.
high_performers = []
for emp in employees:
    if emp[2] > 75:
        high_performers.append(emp[1])

print("High Performers:", high_performers)

print("-" * 40)

# ----------------------------------------
# Task 5: Display performance category for each employee
# Assign category based on the defined score ranges.
print("Performance Categories:")
for emp in employees:
    score = emp[2]

    if score >= 90:
        category = "Excellent"
    elif score >= 75:
        category = "Good"
    elif score >= 60:
        category = "Average"
    else:
        category = "Needs Improvement"

    print(emp[1], "->", category)
