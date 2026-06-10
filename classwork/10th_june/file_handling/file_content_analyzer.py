# --------------------------------------------------
# File Content Analyzer
# --------------------------------------------------

# Function to count vowels in the file content
def count_vowels(content):

    vowels = "aeiouAEIOU"
    count = 0

    # Check each character
    for ch in content:

        if ch in vowels:
            count += 1

    return count


# Function to count total characters
def count_characters(content):

    return len(content)


# Function to count total lines
def count_lines(content):

    # splitlines() converts text into a list of lines
    lines = content.splitlines()

    return len(lines)


# --------------------------------------------------
# Main Program
# --------------------------------------------------

# Open the file in read mode
file = open("article.txt", "r")

# Read complete file content
content = file.read()

# Close the file
file.close()

# Call functions
total_vowels = count_vowels(content)
total_characters = count_characters(content)
total_lines = count_lines(content)

# Display Report
print("File Analysis Report")

print("\nTotal Number of Vowels    :", total_vowels)
print("Total Number of Characters:", total_characters)
print("Total Number of Lines     :", total_lines)
