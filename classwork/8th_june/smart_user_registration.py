# Smart User Registration System

# Taking input from the user

name = input("Enter Full Name: ")
email = input("Enter Email ID: ")

# ----------------------------------
# Task 1: Display name in uppercase

print("\nName in Uppercase:", name.upper())

# ----------------------------------
# Task 2: Display name in title case

print("Name in Title Case:", name.title())

# ----------------------------------
# Task 3: Count total characters in the name

print("Total Characters:", len(name))

# ----------------------------------
# Task 4: Count the number of spaces

print("Spaces:", name.count(" "))

# ----------------------------------
# Task 5: Check whether email contains "@"

if "@" in email:
    print("Valid Email: Yes")
else:
    print("Valid Email: No")

# ----------------------------------
# Task 6: Check whether email ends with ".com"

if email.endswith(".com"):
    print("Ends With .com: Yes")
else:
    print("Ends With .com: No")

# ----------------------------------
# Task 7: Extract company name from email

company_name = email.split("@")[1].split(".")[0]

print("Company Name:", company_name)

# ----------------------------------
# Task 8: Replace spaces with underscores

new_name = name.replace(" ", "_")

print("Name with Underscore:", new_name)

# ----------------------------------
# Task 9: Check whether name starts with 'A'

print("Starts With A:", name.upper().startswith("A"))

# ----------------------------------
# Task 10: Count how many times 'a' appears

count_a = name.lower().count("a")

print("Count of 'a':", count_a)
