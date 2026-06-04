balance = 10000

# Simple ATM Simulation
while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

# Get user choice
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance: ₹", balance)

# Handle deposit operations
    elif choice == 2:
        amount = float(input("Enter amount to deposit: ₹"))
        balance += amount
        print("₹", amount, "deposited successfully.")
        print("Updated Balance: ₹", balance)

# Handle withdrawal operations
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: ₹"))

        if amount <= balance:
            balance -= amount
            print("₹", amount, "withdrawn successfully.")
            print("Remaining Balance: ₹", balance)
        else:
            print("Insufficient Balance!")

    elif choice == 4:
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid Choice! Please try again.")