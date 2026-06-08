# Employee Performance Dashboard

# Dictionary containing employee IDs and performance scores
performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# ----------------------------------
# Task 1: Display employees scoring above 80

print("Employees Scoring Above 80:")

for emp in performance:
    if performance[emp] > 80:
        print(emp)

# ----------------------------------
# Task 2: Count employees needing improvement

count = 0

for emp in performance:
    if performance[emp] < 60:
        count += 1

print("\nEmployees Needing Improvement:", count)

# ----------------------------------
# Task 3: Find the top performer

top_employee = ""
highest_score = 0

for emp in performance:
    if performance[emp] > highest_score:
        highest_score = performance[emp]
        top_employee = emp

print("\nTop Performer:")
print(top_employee, "(", highest_score, ")")

# ----------------------------------
# Task 4: Calculate average performance score

total_score = 0

for emp in performance:
    total_score += performance[emp]

average_score = total_score / len(performance)

print("\nAverage Score:", average_score)

# ----------------------------------
# Task 5: Create separate lists

excellent = []
good = []
average = []
poor = []

for emp in performance:

    score = performance[emp]

    if score >= 90:
        excellent.append(emp)

    elif score >= 75:
        good.append(emp)

    elif score >= 60:
        average.append(emp)

    else:
        poor.append(emp)

print("\nExcellent:", excellent)
print("Good:", good)
print("Average:", average)
print("Poor:", poor)
