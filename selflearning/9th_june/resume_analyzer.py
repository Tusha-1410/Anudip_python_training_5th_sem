# --------------------------------------------------
# Student Resume Analyzer
# --------------------------------------------------

# Sample Resume Text
# (Student can replace this with their own resume)

resume = """
Name: Rahul Sharma

Email: rahul123@gmail.com
Phone: 9876543210

Education:
Bachelor of Technology in Computer Science

Skills:
Python SQL Java React Python SQL Communication

Projects:
Student Management System using Python
Online Shopping Website using React

Achievements:
Won Coding Competition
Completed Python Certification
Excellent Communication Skills
"""

# --------------------------------------------------
# Count Total Words

words = resume.split()

total_words = len(words)

# --------------------------------------------------
# Count Total Characters

total_characters = len(resume)

# --------------------------------------------------
# Extract Email IDs

emails = []

for word in words:

    if "@" in word and "." in word:
        emails.append(word)

# --------------------------------------------------
# Extract Phone Numbers

phone_numbers = []

for word in words:

    # Check if word contains only digits
    # and has 10 digits

    if word.isdigit() and len(word) == 10:
        phone_numbers.append(word)

# --------------------------------------------------
# Skills List
# (Can be modified according to requirement)

skill_list = [
    "Python",
    "SQL",
    "Java",
    "React",
    "Communication",
    "C",
    "C++",
    "HTML",
    "CSS"
]

# --------------------------------------------------
# Count Skills Mentioned

skill_frequency = {}

for skill in skill_list:

    count = 0

    for word in words:

        if word.lower() == skill.lower():

            count += 1

    if count > 0:

        skill_frequency[skill] = count

# --------------------------------------------------
# Count Total Skills Mentioned

total_skills = len(skill_frequency)

# --------------------------------------------------
# Word Frequency Dictionary

word_frequency = {}

for word in words:

    word = word.strip(",.:").lower()

    if word in word_frequency:

        word_frequency[word] += 1

    else:

        word_frequency[word] = 1

# --------------------------------------------------
# Find Repeated Keywords

repeated_keywords = []

for word in word_frequency:

    if word_frequency[word] > 1:

        repeated_keywords.append(word)

# --------------------------------------------------
# Find Most Frequently Used Word

most_common_word = ""
highest_count = 0

for word in word_frequency:

    if word_frequency[word] > highest_count:

        highest_count = word_frequency[word]

        most_common_word = word

# --------------------------------------------------
# Detect Duplicate Skills

duplicate_skills = []

for skill in skill_frequency:

    if skill_frequency[skill] > 1:

        duplicate_skills.append(skill)

# --------------------------------------------------
# Top 5 Keywords

top_keywords = []

# Copy dictionary

temp_dict = word_frequency.copy()

for i in range(5):

    max_word = ""
    max_count = 0

    for word in temp_dict:

        if temp_dict[word] > max_count:

            max_count = temp_dict[word]

            max_word = word

    if max_word != "":

        top_keywords.append(max_word)

        del temp_dict[max_word]

# --------------------------------------------------
# Most Frequent Skill

most_frequent_skill = ""

highest_skill_count = 0

for skill in skill_frequency:

    if skill_frequency[skill] > highest_skill_count:

        highest_skill_count = skill_frequency[skill]

        most_frequent_skill = skill

# --------------------------------------------------
# Display Report

print("\n================================")
print("RESUME ANALYSIS REPORT")
print("================================")

print("Total Words      :", total_words)

print("Total Characters :", total_characters)

print()

print("Email IDs Found  :", len(emails))

for email in emails:
    print(email)

print()

print("Phone Numbers Found :", len(phone_numbers))

for number in phone_numbers:
    print(number)

print()

print("Skills Mentioned :", total_skills)

print("Most Frequent Skill :", most_frequent_skill)

print()

print("Repeated Keywords :")

for keyword in repeated_keywords:
    print(keyword, end=" ")

print()

print("\nDuplicate Skills :")

for skill in duplicate_skills:
    print(skill, end=" ")

print()

print("\nSkill Frequency Report")

for skill in skill_frequency:

    print(skill, "->", skill_frequency[skill])

print()

print("Top 5 Keywords :")

for keyword in top_keywords:

    print(keyword, end=" ")

print()

print("\nMost Frequently Used Word :",
      most_common_word)
      