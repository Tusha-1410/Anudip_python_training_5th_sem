# List to store scores for each player
scores = []

# Collect scores for 11 players (players numbered 1 to 11)
for i in range(1, 12):
    while True:
        # Prompt the user for the player's score and convert to integer
        score = int(input(f"Enter score of Player {i}: "))

        # Only accept non-negative scores
        if score >= 0:
            scores.append(score)  # save valid score and exit the loop
            break
        else:
            # Inform the user and repeat the prompt on invalid input
            print("Invalid Score! Enter a non-negative score.")

# Display all collected scores
print("\nScores of All Players:")

for i in range(11):
    # Index i corresponds to player number (i+1)
    print(f"Player {i+1}: {scores[i]}")

#finding maximum score
max_score = scores[0]  # Initialize max_score with the first player's score
for score in scores:
    if score > max_score:
        max_score = score
print(f"\nMaximum Score: {max_score}")
