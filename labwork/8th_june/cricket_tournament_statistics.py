# Cricket Tournament Statistics

# Dictionary containing player names and runs scored
runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

# ----------------------------------
# Task 1: Display players scoring more than 500 runs

print("Players Scoring More Than 500 Runs:")

for player in runs:
    if runs[player] > 500:
        print(player)

# ----------------------------------
# Task 2: Find the Orange Cap winner

orange_cap = ""
highest_runs = 0

for player in runs:
    if runs[player] > highest_runs:
        highest_runs = runs[player]
        orange_cap = player

print("\nOrange Cap Winner:")
print(orange_cap, "(", highest_runs, ")")

# ----------------------------------
# Task 3: Find the lowest scorer

lowest_scorer = ""
lowest_runs = 9999

for player in runs:
    if runs[player] < lowest_runs:
        lowest_runs = runs[player]
        lowest_scorer = player

print("\nLowest Scorer:")
print(lowest_scorer, "(", lowest_runs, ")")

# ----------------------------------
# Task 4: Calculate total runs scored

total_runs = 0

for player in runs:
    total_runs += runs[player]

print("\nTotal Tournament Runs:", total_runs)

# ----------------------------------
# Task 5: Create a list of players scoring below 400

below_400 = []

for player in runs:
    if runs[player] < 400:
        below_400.append(player)

print("\nPlayers Scoring Below 400:")
print(below_400)

# ----------------------------------
# Task 6: Count players scoring between 400 and 600 runs

count = 0

for player in runs:
    if runs[player] >= 400 and runs[player] <= 600:
        count += 1

print("\nPlayers Between 400 and 600 Runs:", count)

