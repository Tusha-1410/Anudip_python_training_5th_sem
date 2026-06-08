# Email Address Validator

# Taking email as input
email = input("Enter Email Address: ")

# ----------------------------------
# Task 1: Extract username

username = email.split("@")[0]

print("\nUsername:", username)

# ----------------------------------
# Task 2: Extract domain name

domain = email.split("@")[1].split(".")[0]

print("Domain:", domain)

# ----------------------------------
# Task 3: Extract extension

extension = email.split(".")[-1]

print("Extension:", extension)

# ----------------------------------
# Task 4: Count digits present in username

digit_count = 0

for ch in username:
    if ch.isdigit():
        digit_count += 1

print("\nDigits Found:", digit_count)

# ----------------------------------
# Task 5: Count special characters

special_count = 0

for ch in email:
    if not ch.isalnum():
        special_count += 1

print("Special Characters Found:", special_count)

# ----------------------------------
# Task 6: Validate email

# Check if exactly one @ exists
at_count = email.count("@")

# Check if . exists after @
dot_after_at = False

if "@" in email:
    position = email.index("@")

    if "." in email[position:]:
        dot_after_at = True

# ----------------------------------
# Task 7: Display email status

if at_count == 1 and dot_after_at:
    print("\nEmail Status: Valid")
else:
    print("\nEmail Status: Invalid")
    