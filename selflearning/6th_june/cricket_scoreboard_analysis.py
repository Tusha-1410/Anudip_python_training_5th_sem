# Cricket Scoreboard Analysis

# Dictionary containing player names and their scores
scores = {
    "Virat": 78,
    "Rohit": 112,
    "Gill": 45,
    "Rahul": 89,
    "Hardik": 32,
    "Jadeja": 61,
    "Surya": 105,
    "Pant": 95,
    "Bumrah": 18,
    "Shami": 25
}

# ----------------------------------
# Task 1: Display players who scored 50 or more runs

print("Players who scored 50 or more runs:")

for player in scores:
    if scores[player] >= 50:
        print(player, "-", scores[player])

# ----------------------------------
# Task 2: Count the number of centuries

century_count = 0

for player in scores:
    if scores[player] >= 100:
        century_count += 1

print("\nNumber of Centuries:", century_count)

# ----------------------------------
# Task 3: Find the player with the highest score

highest_player = ""
highest_score = 0

for player in scores:
    if scores[player] > highest_score:
        highest_score = scores[player]
        highest_player = player

print("\nPlayer with Highest Score:")
print(highest_player, "-", highest_score)

# ----------------------------------
# Task 4: Create a list of players scoring below 30 runs

low_scorers = []

for player in scores:
    if scores[player] < 30:
        low_scorers.append(player)

print("\nPlayers Scoring Below 30 Runs:")
print(low_scorers)

# ----------------------------------
# Task 5: Count players scoring between 50 and 99

count = 0

for player in scores:
    if scores[player] >= 50 and scores[player] <= 99:
        count += 1

print("\nPlayers Scoring Between 50 and 99 Runs:", count)
