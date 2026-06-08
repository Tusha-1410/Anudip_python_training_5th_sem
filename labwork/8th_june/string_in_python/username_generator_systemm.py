# Username Generator System

# Taking student's name as input
name = input("Enter Your Name: ")

# ----------------------------------
# Task 1: Remove spaces

username = name.replace(" ", "")

# ----------------------------------
# Task 2: Convert to lowercase

username = username.lower()

# ----------------------------------
# Task 3: Append current year

username = username + "2026"

# Display generated username
print("\nGenerated Username:", username)

# ----------------------------------
# Task 4: If username length exceeds 12,
# keep only first 12 characters

if len(username) > 12:
    short_username = username[:12]
    print("Shortened Username:", short_username)

# ----------------------------------
# Task 5 and 6: Count vowels and consonants

vowels = 0
consonants = 0

for ch in username:

    if ch.isalpha():

        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

# ----------------------------------
# Task 7: Display username statistics

print("\nOriginal Name:", name)
print("Username Length:", len(username))
print("Vowels:", vowels)
print("Consonants:", consonants)

print("\nStatus: Username Generated Successfully")
