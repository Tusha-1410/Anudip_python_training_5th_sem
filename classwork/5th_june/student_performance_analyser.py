# List of marks for 8 students
marks = [78, 45, 92, 35, 88, 40, 99, 56]

# List to store marks of students who passed (mark >= 40)
passed_students = []
# Counter for students who failed (mark < 40)
failed_count = 0
# List to store marks of students in the merit list (mark > 75)
merit_list = []

# Initialize highest and lowest marks from the first student's mark
highest = marks[0]
lowest = marks[0]

# Iterate through each mark in the marks list
for mark in marks:
    # Check if student passed (marks >= 40 is passing)
    if mark >= 40:
        # Add the passing mark to the passed_students list
        passed_students.append(mark)
    else:
        # Increment the counter for failed students
        failed_count += 1

    # Check if current mark is higher than the highest recorded mark
    if mark > highest:
        # Update highest mark
        highest = mark

    # Check if current mark is lower than the lowest recorded mark
    if mark < lowest:
        # Update lowest mark
        lowest = mark

    # Check if the mark qualifies for merit list (mark > 75)
    if mark > 75:
        # Add the merit mark to the merit_list
        merit_list.append(mark)

# Display all analyzed results
print("Passed Students:", passed_students)
print("Failed Count:", failed_count)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Merit List:", merit_list)
