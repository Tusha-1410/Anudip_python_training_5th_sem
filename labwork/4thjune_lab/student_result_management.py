total = 0
fail_count = 0

# Collect marks for 5 subjects and calculate total and fail count
for i in range(1, 6):
    marks = int(input(f"Enter marks of Subject {i}: "))
    total += marks

# Check if the marks are less than 40 to count as a fail
    if marks < 40:
        fail_count += 1

percentage = total / 5

# Determine the grade based on percentage and fail count
if fail_count > 0:
    grade = "Fail"
elif percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

print("\nTotal Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Number of Subjects Failed:", fail_count)
