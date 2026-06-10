# Cricket Tournament Analytics System

# Dictionary of players with their tournament statistics.
# Each player record tracks total runs, matches played, and wickets taken.
players = {
    "Virat": {"runs": 645, "matches": 12, "wickets": 0},
    "Rohit": {"runs": 580, "matches": 12, "wickets": 1},
    "Gill": {"runs": 520, "matches": 11, "wickets": 0},
    "Rahul": {"runs": 430, "matches": 10, "wickets": 0},
    "Iyer": {"runs": 390, "matches": 11, "wickets": 2},
    "Hardik": {"runs": 350, "matches": 10, "wickets": 8},
    "Jadeja": {"runs": 310, "matches": 12, "wickets": 15},
    "Ashwin": {"runs": 220, "matches": 10, "wickets": 18},
    "Bumrah": {"runs": 80, "matches": 12, "wickets": 22},
    "Shami": {"runs": 60, "matches": 11, "wickets": 20},
    "Siraj": {"runs": 45, "matches": 10, "wickets": 17},
    "Kuldeep": {"runs": 95, "matches": 11, "wickets": 19},
    "Pant": {"runs": 480, "matches": 10, "wickets": 0},
    "Surya": {"runs": 510, "matches": 12, "wickets": 1},
    "Rinku": {"runs": 340, "matches": 9, "wickets": 0},
    "Samson": {"runs": 410, "matches": 10, "wickets": 0},
    "Jaiswal": {"runs": 530, "matches": 11, "wickets": 0},
    "Gaikwad": {"runs": 470, "matches": 10, "wickets": 0},
    "Axar": {"runs": 280, "matches": 11, "wickets": 12},
    "Chahal": {"runs": 40, "matches": 10, "wickets": 16},
    "Ishan": {"runs": 360, "matches": 9, "wickets": 0},
    "Washington": {"runs": 240, "matches": 10, "wickets": 10},
    "Arshdeep": {"runs": 30, "matches": 10, "wickets": 14},
    "Prasidh": {"runs": 25, "matches": 8, "wickets": 11},
    "Avesh": {"runs": 20, "matches": 8, "wickets": 9},
    "Mukesh": {"runs": 15, "matches": 7, "wickets": 8},
    "Tilak": {"runs": 320, "matches": 9, "wickets": 1},
    "Abhishek": {"runs": 370, "matches": 9, "wickets": 2},
    "Nitish": {"runs": 300, "matches": 8, "wickets": 6},
    "Varun": {"runs": 50, "matches": 10, "wickets": 21}
}

# 1. Display all player statistics
# Print each player and their complete stats.
print("\nALL PLAYER STATISTICS")

for player in players:
    print(player, players[player])

# 2. Highest Run Scorer
# Find the player with the most runs by scanning the list.
first = True

for player in players:

    if first:
        highest = player
        first = False

    elif players[player]["runs"] > players[highest]["runs"]:
        highest = player

print("\nHighest Run Scorer")
print(highest, players[highest])

# 3. Lowest Run Scorer
# Find the player with the fewest runs scored in the tournament.
first = True

for player in players:

    if first:
        lowest = player
        first = False

    elif players[player]["runs"] < players[lowest]["runs"]:
        lowest = player

print("\nLowest Run Scorer")
print(lowest, players[lowest])

# 4. Average Runs
# Calculate the tournament run average across all players.
total_runs = 0

for player in players:
    total_runs += players[player]["runs"]

average_runs = total_runs / len(players)

print("\nAverage Runs =", round(average_runs, 2))

# 5. Player with Maximum Wickets
# Determine the bowler with the highest wicket tally.
first = True

for player in players:

    if first:
        wicket_king = player
        first = False

    elif players[player]["wickets"] > players[wicket_king]["wickets"]:
        wicket_king = player

print("\nMaximum Wickets")
print(wicket_king, players[wicket_king])

# 6. All-Rounders

print("\nALL-ROUNDERS")

for player in players:

    if players[player]["runs"] > 300 and players[player]["wickets"] > 5:
        print(player, players[player])

# 7. Players Scoring Above Average

print("\nABOVE AVERAGE RUN SCORERS")

for player in players:

    if players[player]["runs"] > average_runs:
        print(player, players[player]["runs"])

# 8. Categories

print("\nPLAYER CATEGORIES")

for player in players:

    runs = players[player]["runs"]

    if runs >= 500:
        category = "Star Performer"

    elif runs >= 350:
        category = "Good Performer"

    elif runs >= 200:
        category = "Average Performer"

    else:
        category = "Poor Performer"

    print(player, "-", category)

# 9. Team Statistics

total_wickets = 0

for player in players:
    total_wickets += players[player]["wickets"]

print("\nTEAM STATISTICS")

print("Total Players =", len(players))
print("Total Runs =", total_runs)
print("Total Wickets =", total_wickets)
print("Average Runs =", round(average_runs, 2))

# 10. Top 5 Batsmen

print("\nTOP 5 BATSMEN")

temp_players = {}

for player in players:
    temp_players[player] = players[player]

for i in range(5):

    first = True

    for player in temp_players:

        if first:
            top_batsman = player
            first = False

        elif temp_players[player]["runs"] > temp_players[top_batsman]["runs"]:
            top_batsman = player

    print(i + 1,
          top_batsman,
          temp_players[top_batsman]["runs"])

    del temp_players[top_batsman]

# 11. Top 5 Bowlers

print("\nTOP 5 BOWLERS")

temp_players = {}

for player in players:
    temp_players[player] = players[player]

for i in range(5):

    first = True

    for player in temp_players:

        if first:
            top_bowler = player
            first = False

        elif temp_players[player]["wickets"] > temp_players[top_bowler]["wickets"]:
            top_bowler = player

    print(i + 1,
          top_bowler,
          temp_players[top_bowler]["wickets"])

    del temp_players[top_bowler]

# 12. Award Winners Dictionary

award_winners = {}

for player in players:

    if players[player]["runs"] > 500 or players[player]["wickets"] > 15:
        award_winners[player] = players[player]

print("\nAWARD WINNERS")

for player in award_winners:
    print(player, award_winners[player])

# CHALLENGE : Tournament Report

print("\n========== TOURNAMENT REPORT ==========")

print("Total Players =", len(players))
print("Total Runs =", total_runs)
print("Total Wickets =", total_wickets)

print("\nHighest Run Scorer:")
print(highest)

print("\nHighest Wicket Taker:")
print(wicket_king)

print("\nAward Winners Count =", len(award_winners))

print("\nTournament Analysis Completed Successfully")
