amount = int(input("Enter the amount: "))

# Validation: amount must be positive
if amount <= 0:
    print("Invalid Amount! Enter a positive amount.")
else:
    # Available note denominations in descending order
    notes = [500, 200, 100, 50, 20, 10]

    print("Minimum Notes Required:")

    # Greedy approach: use the largest notes first to minimize total count
    for note in notes:
        # Calculate how many of this note value can be used
        count = amount // note

        # If at least one note can be used, print the denomination and count
        if count > 0:
            print(f"₹{note} x {count}")

        # Update remaining amount after using the current note denomination
        amount = amount % note

