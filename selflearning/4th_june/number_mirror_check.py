num = input("Enter a number: ")

# Validation: ensure input contains only digits
if not num.isdigit():
    print("Invalid Input! Enter digits only.")
# Validation: require an even number of digits to split into two equal halves
elif len(num) % 2 != 0:
    print("Invalid Input! Number must have an even number of digits.")
else:
    # Compute the midpoint to split the string into two halves
    mid = len(num) // 2

    # Left half is the first mid digits, right half is the remaining digits
    left_half = num[:mid]
    right_half = num[mid:]

    # If both halves are identical, it's a Mirror Number
    if left_half == right_half:
        print("Mirror Number")
    else:
        print("Not a Mirror Number")
        