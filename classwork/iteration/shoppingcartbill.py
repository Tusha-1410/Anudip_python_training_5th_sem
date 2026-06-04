total_bill = 0

while True:
    price = float(input("Enter Item Price: "))

    if price < 0:
        print("Invalid Price! Price cannot be negative.")
        continue

    if price == 0:
        break

    total_bill += price

print("Total Bill Amount: ₹", total_bill)