# Cricket Tournament Scorecard Analysis

# List containing batsman's scores in different matches
scores = [45, 78, 12, 100, 67, 8, 90, 55]

# ----------------------------------------
# Task 1: Count Half-Centuries and Centuries

half_centuries = 0
centuries = 0

for score in scores:

    # Score between 50 and 99 is a half-century
    if score >= 50 and score < 100:
        half_centuries += 1

    # Score 100 or more is a century
    elif score >= 100:
        centuries += 1

print("Half-Centuries:", half_centuries)
print("Centuries:", centuries)

print("-" * 40)

# ----------------------------------------
# Task 2: Find the Highest Score

# Assume first score is the highest
highest_score = scores[0]

# Compare every score with current highest score
for score in scores:
    if score > highest_score:
        highest_score = score

print("Highest Score:", highest_score)

print("-" * 40)

# ----------------------------------------
# Task 3: Display Scores Below 20

print("Scores Below 20:")

for score in scores:
    if score < 20:
        print(score)

print("-" * 40)

# ----------------------------------------
# Task 4: Calculate Average Score

total = 0

# Add all scores
for score in scores:
    total += score

# Average = Total Scores / Number of Matches
average = total / len(scores)

print("Average Score:", average)

print("-" * 40)
