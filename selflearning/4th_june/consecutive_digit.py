# Read an integer from the user
num = int(input("Enter a number: "))

# Validation: ensure the input is a positive number
if num <= 0:
    print("Invalid Input! Please enter a positive number.")
else:
    # Convert the number to a string so each digit can be checked
    num_str = str(num)
    is_consecutive = True

    # Compare each digit with the next one
    for i in range(len(num_str) - 1):
        # If the next digit is not exactly one greater, it is not consecutive
        if int(num_str[i + 1]) != int(num_str[i]) + 1:
            is_consecutive = False
            break

    # Print the final result
    if is_consecutive:
        print("Consecutive Number")
    else:
        print("Not a Consecutive Number")