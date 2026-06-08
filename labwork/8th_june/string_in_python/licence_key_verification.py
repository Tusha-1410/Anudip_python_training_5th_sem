# License Key Verification System

# Taking license key as input
license_key = input("Enter License Key: ")

# ----------------------------------
# Task 1: Create a list containing all groups

groups = license_key.split("-")

print("\nGroups:", groups)

# ----------------------------------
# Task 2: Verify there are exactly 4 groups

print("Number of Groups:", len(groups))

# ----------------------------------
# Task 3: Count total letters

letter_count = 0

for ch in license_key:

    if ch.isalpha():
        letter_count += 1

print("Total Letters:", letter_count)

# ----------------------------------
# Task 4: Count vowels

vowel_count = 0

for ch in license_key:

    if ch.upper() in "AEIOU":
        vowel_count += 1

print("Total Vowels:", vowel_count)

# ----------------------------------
# Task 5: Remove hyphens and display merged key

merged_key = license_key.replace("-", "")

print("Merged Key:", merged_key)

# ----------------------------------
# Task 6: Check whether each group contains 4 characters

group_valid = True

for group in groups:

    if len(group) != 4:
        group_valid = False

# ----------------------------------
# Task 7: Display whether the key format is valid

if len(groups) == 4 and group_valid:
    print("\nLicense Key Status: Valid")
else:
    print("\nLicense Key Status: Invalid")
    