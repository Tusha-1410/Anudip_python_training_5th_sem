# --------------------------------------------------
# News Article Text Analyzer
# --------------------------------------------------

# Sample News Article (You can replace with any 300+ word article)

article = """
Technology is changing the world rapidly. Artificial intelligence is being
used in healthcare, education, transportation, and many other industries.
Many companies are investing heavily in research and development. Technology
helps people communicate faster and access information easily. Education is
becoming more digital with online learning platforms. Healthcare systems are
using advanced tools to improve patient care. Transportation services are
becoming smarter with automation and data analysis.

The use of technology has increased productivity in businesses. Employees can
collaborate from different locations using digital tools. Governments are
also adopting digital services to improve public administration. Smart cities
are being developed to provide better infrastructure and services. Renewable
energy technologies are helping reduce environmental impact. Scientists are
working on innovative solutions to address global challenges.

Despite many benefits, technology also brings challenges. Cybersecurity
threats are increasing as more data is stored online. Organizations must
protect sensitive information from unauthorized access. Digital literacy is
important for individuals to use technology safely and effectively.
Technology will continue to shape the future and influence daily life.
"""

# --------------------------------------------------
# Count Total Characters

total_characters = len(article)

# --------------------------------------------------
# Convert article into list of words

words = article.lower().split()

# Count Total Words

total_words = len(words)

# --------------------------------------------------
# Count Total Sentences

total_sentences = article.count(".") + article.count("!") + article.count("?")

# --------------------------------------------------
# Count Vowels and Consonants

vowels = 0
consonants = 0

for ch in article.lower():

    if ch in "aeiou":
        vowels += 1

    elif ch.isalpha():
        consonants += 1

# --------------------------------------------------
# Find Longest Word

longest_word = words[0]

for word in words:

    clean_word = word.strip(".,!?")

    if len(clean_word) > len(longest_word):
        longest_word = clean_word

# --------------------------------------------------
# Find Shortest Word

shortest_word = words[0]

for word in words:

    clean_word = word.strip(".,!?")

    if len(clean_word) < len(shortest_word):
        shortest_word = clean_word

# --------------------------------------------------
# Create Word Frequency Dictionary

word_frequency = {}

for word in words:

    word = word.strip(".,!?")

    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

# --------------------------------------------------
# Find Most Frequent Word

most_common_word = ""
highest_count = 0

for word in word_frequency:

    if word_frequency[word] > highest_count:

        highest_count = word_frequency[word]
        most_common_word = word

# --------------------------------------------------
# Display Word Frequency Dictionary

print("\nWORD FREQUENCY DICTIONARY")
print(word_frequency)

# --------------------------------------------------
# Words Appearing Only Once

print("\nWORDS APPEARING ONLY ONCE")

for word in word_frequency:

    if word_frequency[word] == 1:
        print(word, end=" ")

print()

# --------------------------------------------------
# Words Appearing More Than 5 Times

print("\nWORDS APPEARING MORE THAN 5 TIMES")

for word in word_frequency:

    if word_frequency[word] > 5:
        print(word, "->", word_frequency[word])

# --------------------------------------------------
# Count Words Starting With Each Alphabet

alphabet_count = {}

for word in word_frequency:

    first_letter = word[0]

    if first_letter in alphabet_count:
        alphabet_count[first_letter] += 1
    else:
        alphabet_count[first_letter] = 1

print("\nWORDS STARTING WITH EACH ALPHABET")

for letter in alphabet_count:
    print(letter, "->", alphabet_count[letter])

# --------------------------------------------------
# Display Unique Words

print("\nUNIQUE WORDS")

for word in word_frequency:
    print(word, end=" ")

print()

# --------------------------------------------------
# Calculate Average Word Length

total_length = 0

for word in words:

    word = word.strip(".,!?")

    total_length += len(word)

average_word_length = total_length / total_words

# --------------------------------------------------
# Vocabulary Size

vocabulary_size = len(word_frequency)

# --------------------------------------------------
# Final Summary Report

print("\n================================")
print("NEWS ARTICLE SUMMARY REPORT")
print("================================")

print("Total Characters     :", total_characters)
print("Total Words          :", total_words)
print("Total Sentences      :", total_sentences)

print("Vowels              :", vowels)
print("Consonants          :", consonants)

print("Longest Word        :", longest_word)
print("Shortest Word       :", shortest_word)

print("Most Frequent Word  :", most_common_word)

print("Average Word Length :", round(average_word_length, 2))

print("Vocabulary Size     :", vocabulary_size)
