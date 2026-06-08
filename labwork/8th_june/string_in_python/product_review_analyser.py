# Product Review Analyzer

# Review stored in a variable
review = "This product is excellent excellent excellent and very useful"

# Convert review into a list of words
words = review.split()

# ----------------------------------
# Task 1: Count total words

print("Total Words:", len(words))

# ----------------------------------
# Task 2: Create a dictionary containing word frequencies

frequency = {}

for word in words:

    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequencies:")

for word in frequency:
    print(word, "->", frequency[word])

# ----------------------------------
# Task 3: Find the most frequently used word

most_frequent_word = ""
highest_count = 0

for word in frequency:

    if frequency[word] > highest_count:
        highest_count = frequency[word]
        most_frequent_word = word

print("\nMost Frequent Word:", most_frequent_word)

# ----------------------------------
# Task 4: Find all words appearing only once

single_words = []

for word in frequency:

    if frequency[word] == 1:
        single_words.append(word)

print("\nWords Appearing Once:")
print(single_words)

# ----------------------------------
# Task 5: Count words having more than 5 characters

count = 0

for word in words:

    if len(word) > 5:
        count += 1

print("\nWords Having More Than 5 Characters:", count)

# ----------------------------------
# Task 6: Display words in reverse order

print("\nWords in Reverse Order:")

for word in words[::-1]:
    print(word, end=" ")

# ----------------------------------
# Task 7: Create a list of unique words

unique_words = []

for word in words:

    if word not in unique_words:
        unique_words.append(word)

print("\n\nUnique Words:")
print(unique_words)
