# --------------------------------------------------
# Password Security Analyzer
# --------------------------------------------------

# Counters for the final report
# These variables keep track of the strength distribution across all passwords.
strong_count = 0
medium_count = 0
weak_count = 0

# Total passwords to analyze
# The script will prompt the user exactly this many times.
total_passwords = 15

# --------------------------------------------------
# Analyze passwords one by one
for i in range(1, total_passwords + 1):

    print("\n================================")
    print("Password", i)
    print("================================")

    password = input("Enter Password: ")

    # Initialize counters for this password
    uppercase = 0
    lowercase = 0
    digits = 0
    special = 0
    vowels = 0
    consonants = 0

    # Dictionary to count how often each character appears
    frequency = {}

    # ------------------------------------------
    # Analyze each character in the password
    for ch in password:

        # Count uppercase letters
        if ch.isupper():
            uppercase += 1

        # Count lowercase letters
        elif ch.islower():
            lowercase += 1

        # Count digits
        elif ch.isdigit():
            digits += 1

        # Count special characters for everything else
        else:
            special += 1

        # --------------------------------------
        # Count vowels and consonants separately
        if ch.lower() in "aeiou":
            vowels += 1
        elif ch.isalpha():
            consonants += 1

        # --------------------------------------
        # Update character frequency dictionary
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    # ------------------------------------------
    # Check whether the entered password has a valid length
    if len(password) >= 8:
        length_status = "Valid"
    else:
        length_status = "Too Short"

    # ------------------------------------------
    # Check whether the password contains spaces
    if " " in password:
        space_status = "Yes"
    else:
        space_status = "No"

    # ------------------------------------------
    # Determine Password Strength
    # Strong: length >= 8, contains upper/lower/digit/special, and no spaces.
    # Medium: length >= 8 but missing one or more required character classes.
    # Weak: shorter than 8 characters.
    if (len(password) >= 8 and
            uppercase > 0 and
            lowercase > 0 and
            digits > 0 and
            special > 0 and
            space_status == "No"):

        strength = "Strong"
        strong_count += 1

    elif len(password) >= 8:

        strength = "Medium"
        medium_count += 1

    else:

        strength = "Weak"
        weak_count += 1

    # ------------------------------------------
    # Find characters that appear more than once
    repeated = []

    for ch in frequency:
        if frequency[ch] > 1:
            repeated.append(ch)

    # ------------------------------------------
    # Find the most frequent character in the password
    most_common = ""
    highest_count = 0

    for ch in frequency:
        if frequency[ch] > highest_count:
            highest_count = frequency[ch]
            most_common = ch

    # ------------------------------------------
    # Display the analysis report for this password
    print("\nPassword Analysis")

    print("Uppercase Letters :", uppercase)
    print("Lowercase Letters :", lowercase)
    print("Digits            :", digits)
    print("Special Characters:", special)

    print("Length Check      :", length_status)
    print("Contains Spaces   :", space_status)

    print("Vowels            :", vowels)
    print("Consonants        :", consonants)

    print("Password Strength :", strength)
    print("Repeated Characters:", repeated)
    print("Most Frequent Character:", most_common, "(" + str(highest_count) + " times )")

# --------------------------------------------------
# Final Security Report
# Print the total counts after all passwords have been evaluated.
print("\n================================")
print("FINAL SECURITY REPORT")
print("================================")

print("Total Passwords Analyzed :", total_passwords)
print("Strong Passwords :", strong_count)
print("Medium Passwords :", medium_count)
print("Weak Passwords   :", weak_count)
