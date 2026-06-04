import random

#system generates a random number between 1 and 50
secret_number = random.randint(1, 50)
attempts = 0

while True:
    guess = int(input("Enter your guess (1-50): "))
    attempts += 1

#compare the user's guess with the secret number and provide feedback
    if guess > secret_number:
        print("Too High")
    elif guess < secret_number:
        print("Too Low")
    else:
        print("Correct Guess")
        print("Total Attempts:", attempts)
        break