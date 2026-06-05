code = input("Enter a 6-digit secret code: ")

# Validation: ensure input contains only digits
if not code.isdigit():
    print("Invalid Input! Digits only.")
# Validation: ensure the code has exactly 6 digits
elif len(code) != 6:
    print("Invalid Input! Code must contain exactly 6 digits.")
else:
    # Compute sum of the first three digits
    first_sum = int(code[0]) + int(code[1]) + int(code[2])
    # Compute sum of the last three digits
    last_sum = int(code[3]) + int(code[4]) + int(code[5])

    # If the two sums match, the code is considered valid
    if first_sum == last_sum:
        print("Valid Code")
    else:
        print("Invalid Code")
        