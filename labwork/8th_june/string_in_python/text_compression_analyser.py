# Text Compression Analyzer

# Original text
text = "AAABBBCCCDDDAAA"

print("Original Text:", text)

# ----------------------------------
# Task 1 & 2: Count occurrences and create frequency dictionary

frequency = {}

for ch in text:

    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("\nCharacter Frequencies:")

for ch in frequency:
    print(ch, "->", frequency[ch])

# ----------------------------------
# Task 3: Display unique characters

unique_characters = list(frequency.keys())

print("\nUnique Characters:", unique_characters)

# ----------------------------------
# Task 4: Find the most frequent character

most_frequent = ""
highest_count = 0

for ch in frequency:

    if frequency[ch] > highest_count:
        highest_count = frequency[ch]
        most_frequent = ch

print("\nMost Frequent Character:", most_frequent)

# ----------------------------------
# Task 5: Create compressed output

compressed = ""

count = 1

for i in range(len(text) - 1):

    if text[i] == text[i + 1]:
        count += 1
    else:
        compressed = compressed + text[i] + str(count)
        count = 1

# Add the last character group
compressed = compressed + text[-1] + str(count)

print("Compressed Output:", compressed)

# ----------------------------------
# Task 6: Calculate compression ratio

original_length = len(text)
compressed_length = len(compressed)

compression_ratio = (compressed_length / original_length) * 100

print("\nOriginal Length:", original_length)
print("Compressed Length:", compressed_length)
print("Compression Ratio:", round(compression_ratio, 2), "%")
