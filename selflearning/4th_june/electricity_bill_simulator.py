units = int(input("Enter units consumed: "))

# Validate input: units cannot be negative
if units < 0:
    print("Invalid Input! Units cannot be negative.")
else:
    # Calculate bill according to tariff slabs
    # First 100 units: ₹5 per unit
    # Next 100 units (101-200): ₹7 per unit
    # Above 200 units: ₹10 per unit
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)
    else:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

    # Apply a 10% surcharge if the bill exceeds ₹5000
    if bill > 5000:
        surcharge = bill * 0.10
        bill += surcharge
        print("Surcharge Applied: ₹", surcharge)

    # Print the final payable amount
    print("Final Payable Amount: ₹", bill)
    