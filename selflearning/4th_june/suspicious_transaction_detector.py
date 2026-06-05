# Initialize counters and accumulator for transaction analysis
high_transactions = 0  # Count of transactions exceeding ₹50,000
low_transactions = 0   # Count of transactions below ₹1,000
total_amount = 0       # Sum of all transaction amounts

# Continuous loop to process multiple transactions until user terminates
while True:
    amount = float(input("Enter transaction amount (-1 to stop): "))

    # Exit condition: -1 signals the end of transaction input
    if amount == -1:
        break

    # Validation: reject negative amounts (except -1 which signals stop)
    if amount < 0:
        print("Invalid Amount! Enter a positive amount.")
        continue

    # Add this transaction to the total
    total_amount += amount

    # Check if transaction is in the "high" suspicious category
    if amount > 50000:
        high_transactions += 1

    # Check if transaction is in the "low" suspicious category
    if amount < 1000:
        low_transactions += 1

# Display transaction summary after all inputs are collected
print("\nTransaction Summary")
print("Transactions above ₹50,000 =", high_transactions)
print("Transactions below ₹1,000 =", low_transactions)
print("Total Transaction Amount = ₹", total_amount)

