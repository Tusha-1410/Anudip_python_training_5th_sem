secret_number = 7

while True:
    guess = int(input("Guess the Number: "))

    if guess < 1 or guess > 10:
        print("Please enter a number between 1 and 10.")
        continue

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Wrong Guess. Try Again.")