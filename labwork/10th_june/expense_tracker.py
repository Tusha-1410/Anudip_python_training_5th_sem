# --------------------------------------------------
# Daily Expense Tracker and Report Generator
# --------------------------------------------------

# Function to read expenses from file

def read_expenses():

    file = open("expenses.txt", "r")

    expenses = []

    for line in file:

        line = line.strip()

        data = line.split(",")

        expenses.append(data)

    file.close()

    return expenses


# --------------------------------------------------
# Function to save updated expenses back to file

def save_expenses(expenses):

    file = open("expenses.txt", "w")

    for expense in expenses:

        line = expense[0] + "," + expense[1]

        file.write(line + "\n")

    file.close()


# --------------------------------------------------
# Function 1 : Display All Expenses

def display_expenses():

    expenses = read_expenses()

    print("\nExpense Records")

    for expense in expenses:

        print(expense[0], "-> ₹", expense[1])


# --------------------------------------------------
# Function 2 : Calculate Total Expenditure

def total_expenditure():

    expenses = read_expenses()

    total = 0

    for expense in expenses:

        total += int(expense[1])

    print("\nTotal Expenditure = ₹", total)


# --------------------------------------------------
# Function 3 : Highest and Lowest Expense

def highest_lowest_expense():

    expenses = read_expenses()

    highest = expenses[0]
    lowest = expenses[0]

    for expense in expenses:

        if int(expense[1]) > int(highest[1]):
            highest = expense

        if int(expense[1]) < int(lowest[1]):
            lowest = expense

    print("\nHighest Expense")
    print(highest[0], "-> ₹", highest[1])

    print("\nLowest Expense")
    print(lowest[0], "-> ₹", lowest[1])


# --------------------------------------------------
# Function 4 : Expenses Greater Than ₹800

def expenses_above_800():

    expenses = read_expenses()

    print("\nExpenses Greater Than ₹800")

    for expense in expenses:

        if int(expense[1]) > 800:

            print(expense[0], "-> ₹", expense[1])


# --------------------------------------------------
# Function 5 : Add New Expense Category

def add_expense():

    category = input("Enter Expense Category: ")

    amount = input("Enter Amount: ")

    file = open("expenses.txt", "a")

    file.write("\n" + category + "," + amount)

    file.close()

    print("Expense Added Successfully")


# --------------------------------------------------
# Function 6 : Update Existing Expense Amount

def update_expense():

    category = input("Enter Category to Update: ")

    expenses = read_expenses()

    found = False

    for expense in expenses:

        if expense[0].lower() == category.lower():

            new_amount = input("Enter New Amount: ")

            expense[1] = new_amount

            save_expenses(expenses)

            print("Expense Updated Successfully")

            found = True
            break

    if found == False:
        print("Category Not Found")


# --------------------------------------------------
# Function 7 : Generate Summary Report

def generate_report():

    expenses = read_expenses()

    total = 0

    highest = expenses[0]
    lowest = expenses[0]

    above_800 = []

    for expense in expenses:

        amount = int(expense[1])

        total += amount

        if amount > int(highest[1]):
            highest = expense

        if amount < int(lowest[1]):
            lowest = expense

        if amount > 800:
            above_800.append(expense[0])

    file = open("report.txt", "w")

    file.write("Expense Summary Report\n")
    file.write("----------------------\n")

    file.write("Total Expenses : ₹" + str(total) + "\n")

    file.write("Highest Expense Category : "
               + highest[0] + "\n")

    file.write("Lowest Expense Category : "
               + lowest[0] + "\n")

    file.write("\nCategories Spending More Than ₹800\n")

    for category in above_800:

        file.write(category + "\n")

    file.close()

    print("Report Generated Successfully")
    print("Data stored in report.txt")


# --------------------------------------------------
# Main Menu

while True:

    print("\n")
    print("===== Daily Expense Tracker =====")
    print("1. Display All Expenses")
    print("2. Calculate Total Expenditure")
    print("3. Highest and Lowest Expense")
    print("4. Expenses Greater Than ₹800")
    print("5. Add New Expense")
    print("6. Update Expense Amount")
    print("7. Generate Report")
    print("8. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_expenses()

    elif choice == 2:
        total_expenditure()

    elif choice == 3:
        highest_lowest_expense()

    elif choice == 4:
        expenses_above_800()

    elif choice == 5:
        add_expense()

    elif choice == 6:
        update_expense()

    elif choice == 7:
        generate_report()

    elif choice == 8:
        print("Thank You")
        break

    else:
        print("Invalid Choice")
        