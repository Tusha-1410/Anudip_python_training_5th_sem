# Password Strength Analyzer

# Taking password as input
password = input("Enter Password: ")

# Variables to count different character types
upper_count = 0
lower_count = 0
digit_count = 0
special_count = 0

# Lists to store digits and special characters
digit_list = []
special_list = []

# ----------------------------------
# Traverse each character of password

for ch in password:

    # Check uppercase letters
    if ch.isupper():
        upper_count += 1

    # Check lowercase letters
    elif ch.islower():
        lower_count += 1

    # Check digits
    elif ch.isdigit():
        digit_count += 1
        digit_list.append(ch)

    # Otherwise it is a special character
    else:
        special_count += 1
        special_list.append(ch)

# ----------------------------------
# Display counts

print("\nUppercase Letters:", upper_count)
print("Lowercase Letters:", lower_count)
print("Digits:", digit_count)
print("Special Characters:", special_count)

# ----------------------------------
# Display digits and special characters found

print("\nDigits Found:", digit_list)
print("Special Characters Found:", special_list)

# ----------------------------------
# Check password strength

if (len(password) >= 8 and
    upper_count >= 1 and
    lower_count >= 1 and
    digit_count >= 1 and
    special_count >= 1):

    strength = "Strong"

elif len(password) >= 8:
    strength = "Medium"

else:
    strength = "Weak"

# ----------------------------------
# Display result

print("\nPassword Strength:", strength)
