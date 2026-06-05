# List of transactions: positive values are deposits, negative values are withdrawals
transactions = [5000, -2000, 3000, -1000, -500, 7000]

# Initialize current balance and separate lists for deposits and withdrawals
balance = 0
deposits = []
withdrawals = []

# Track the largest deposit and the largest withdrawal
largest_deposit = 0
#deposits are positive 
largest_withdrawal = transactions[1]  # Set initial largest withdrawal to the first withdrawal value

for amount in transactions:
    # Update running balance with each transaction amount
    balance += amount

    if amount > 0:
        # Positive amounts are deposits
        deposits.append(amount)

        # Update the largest deposit if the current amount is bigger
        if amount > largest_deposit:
            largest_deposit = amount

    else:
        # Non-positive amounts are withdrawals
        withdrawals.append(amount)

        # Update the largest withdrawal if the current amount is smaller (more negative)
        if amount < largest_withdrawal:
            largest_withdrawal = amount

# Print the summary of ATM transaction history
print("Current Balance:", balance)
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)
