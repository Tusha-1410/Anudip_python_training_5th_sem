# Online Quiz Evaluation System

# Correct Answers
correct = ['A', 'C', 'B', 'D', 'A']

# Student Answers
student = ['A', 'B', 'B', 'D', 'C']

# ----------------------------------------
# Task 1 & 3: Calculate Score and Count Correct/Wrong Answers

score = 0
correct_count = 0
wrong_count = 0

print("Incorrectly Answered Questions:")

# Compare each student answer with correct answer
for i in range(len(correct)):

    if student[i] == correct[i]:
        score += 1
        correct_count += 1
    else:
        wrong_count += 1

        # Display question number (starts from 1)
        print("Question", i + 1)

print("-" * 40)

# ----------------------------------------
# Display Score

print("Score:", score, "out of", len(correct))
print("Correct Answers:", correct_count)
print("Wrong Answers:", wrong_count)

print("-" * 40)

# ----------------------------------------
# Task 4: Determine Pass/Fail

# Percentage Formula:
# (Score / Total Questions) * 100

percentage = (score / len(correct)) * 100

print("Percentage:", percentage, "%")

# Minimum 60% required to pass
if percentage >= 60:
    print("Result: Pass")
else:
    print("Result: Fail")

print("-" * 40)
