# --------------------------------------------------
# University Course Enrollment Management System
# --------------------------------------------------

# Dictionary storing course enrollments
enrollment = {
    "Python": 45,
    "Java": 38,
    "Data Science": 52,
    "Web Development": 34,
    "Machine Learning": 41,
    "Cloud Computing": 29,
    "Cyber Security": 33,
    "DBMS": 48,
    "Networking": 26,
    "Operating Systems": 37
}

# --------------------------------------------------
# Task 1 : Display Courses Having More Than 40 Enrollments
# --------------------------------------------------

print("Courses with More Than 40 Enrollments:")

for course in enrollment:

    if enrollment[course] > 40:

        print(course)

# --------------------------------------------------
# Task 2 : Find Most and Least Popular Courses
# --------------------------------------------------

most_popular = list(enrollment.keys())[0]
least_popular = list(enrollment.keys())[0]

for course in enrollment:

    if enrollment[course] > enrollment[most_popular]:

        most_popular = course

    if enrollment[course] < enrollment[least_popular]:

        least_popular = course

print("\nMost Popular Course:",
      most_popular,
      "(" + str(enrollment[most_popular]) + " students)")

print("Least Popular Course:",
      least_popular,
      "(" + str(enrollment[least_popular]) + " students)")

# --------------------------------------------------
# Task 3 : Calculate Total Enrollments
# --------------------------------------------------

total_enrollments = 0

for course in enrollment:

    total_enrollments += enrollment[course]

print("\nTotal Enrollments:", total_enrollments)

# --------------------------------------------------
# Task 4 : Categorize Courses
# --------------------------------------------------

high_demand = []
medium_demand = []
low_demand = []

for course in enrollment:

    students = enrollment[course]

    if students > 40:

        high_demand.append(course)

    elif students >= 30:

        medium_demand.append(course)

    else:

        low_demand.append(course)

print("\nHigh Demand:", high_demand)
print("Medium Demand:", medium_demand)
print("Low Demand:", low_demand)

# --------------------------------------------------
# Task 5 : Count Courses Requiring Promotion
# (Enrollments less than 35)
# --------------------------------------------------

promotion_count = 0

for course in enrollment:

    if enrollment[course] < 35:

        promotion_count += 1

print("\nCourses Requiring Promotion:", promotion_count)
