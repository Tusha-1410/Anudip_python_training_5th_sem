# Chat Message Analytics

# Message stored in a variable
message = "Python is awesome and Python is easy to learn"

# ----------------------------------
# Task 1: Count total characters

print("Total Characters:", len(message))

# ----------------------------------
# Task 2: Count total words

words = message.split()

print("Total Words:", len(words))

# ----------------------------------
# Task 3: Find the longest word

longest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest Word:", longest_word)

# ----------------------------------
# Task 4: Find the shortest word

shortest_word = words[0]

for word in words:
    if len(word) < len(shortest_word):
        shortest_word = word

print("Shortest Word:", shortest_word)

# ----------------------------------
# Task 5: Count how many times "Python" appears

python_count = words.count("Python")

print("Occurrences of Python:", python_count)

# ----------------------------------
# Task 6: Create a list of words having more than 4 characters

long_words = []

for word in words:
    if len(word) > 4:
        long_words.append(word)

print("Words Longer Than 4 Characters:", long_words)

# ----------------------------------
# Task 7: Display all words starting with a vowel

vowel_words = []

for word in words:
    if word[0].lower() in "aeiou":
        vowel_words.append(word)

print("Words Starting With a Vowel:", vowel_words)

# ----------------------------------
# Task 8: Count vowels and consonants

vowels = 0
consonants = 0

for ch in message.lower():

    if ch.isalpha():

        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
