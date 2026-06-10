# --------------------------------------------------
# Chat Message Analytics Dashboard
# --------------------------------------------------

# List containing 20 chat messages

messages = [
    "hello how are you",
    "i am doing great today",
    "python programming is interesting",
    "good morning everyone",
    "have a wonderful day",
    "learning python is fun",
    "chat applications are useful",
    "please share the notes",
    "thank you very much",
    "practice makes a person perfect",
    "keep learning new skills",
    "data science is amazing",
    "machine learning is powerful",
    "always stay motivated",
    "hard work brings success",
    "coding improves problem solving",
    "read books regularly",
    "communication skills are important",
    "team work leads to success",
    "never stop learning"
]

# Dictionary to store word frequencies
word_frequency = {}

# Variables for challenge report

longest_message = messages[0]
shortest_message = messages[0]

total_words_all_messages = 0

# --------------------------------------------------
# Analyze each message

for message in messages:

    print("\n================================")
    print("Message :", message)

    # Split message into words

    words = message.split()

    # ------------------------------------------
    # Count words

    total_words = len(words)

    print("Total Words :", total_words)

    # Used later for average calculation
    total_words_all_messages += total_words

    # ------------------------------------------
    # Count characters

    total_characters = len(message)

    print("Total Characters :", total_characters)

    # ------------------------------------------
    # Count vowels and consonants

    vowels = 0
    consonants = 0

    for ch in message.lower():

        if ch in "aeiou":
            vowels += 1

        elif ch.isalpha():
            consonants += 1

    print("Vowels :", vowels)
    print("Consonants :", consonants)

    # ------------------------------------------
    # Find longest word

    longest_word = words[0]

    for word in words:

        if len(word) > len(longest_word):
            longest_word = word

    print("Longest Word :", longest_word)

    # ------------------------------------------
    # Find shortest word

    shortest_word = words[0]

    for word in words:

        if len(word) < len(shortest_word):
            shortest_word = word

    print("Shortest Word :", shortest_word)

    # ------------------------------------------
    # Count word frequencies

    for word in words:

        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    # ------------------------------------------
    # Words starting with vowels

    print("Words Starting With Vowel:")

    for word in words:

        if word[0].lower() in "aeiou":
            print(word, end=" ")

    print()

    # ------------------------------------------
    # Words longer than 5 characters

    print("Words Longer Than 5 Characters:")

    for word in words:

        if len(word) > 5:
            print(word, end=" ")

    print()

    # ------------------------------------------
    # Longest and shortest message

    if len(message) > len(longest_message):
        longest_message = message

    if len(message) < len(shortest_message):
        shortest_message = message

# --------------------------------------------------
# Display Word Frequency Dictionary

print("\n================================")
print("WORD FREQUENCY DICTIONARY")
print("================================")

print(word_frequency)

# --------------------------------------------------
# Display Repeated Words

print("\n================================")
print("REPEATED WORDS")
print("================================")

for word in word_frequency:

    if word_frequency[word] > 1:
        print(word, "->", word_frequency[word])

# --------------------------------------------------
# Find Most Frequently Used Word

most_common_word = ""
highest_count = 0

for word in word_frequency:

    if word_frequency[word] > highest_count:

        highest_count = word_frequency[word]
        most_common_word = word

# --------------------------------------------------
# Calculate Average Words Per Message

average_words = total_words_all_messages / len(messages)

# --------------------------------------------------
# Challenge Report

print("\n================================")
print("CHAT ANALYTICS REPORT")
print("================================")

print("Most Frequently Used Word :",
      most_common_word)

print("Longest Message :",
      longest_message)

print("Shortest Message :",
      shortest_message)

print("Average Words Per Message :",
      round(average_words, 2))
