units = int(input("Enter units consumed: "))

# Calculate the bill based on the given slabs
if units <= 100:
    bill = units * 5
    category = "Low Consumption"

# For units between 101 and 200, the first 100 units are charged at ₹5/unit and the remaining units are charged at ₹7/unit
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
    category = "Medium Consumption"

# For units above 200, the first 100 units are charged at ₹5/unit, the next 100 units are charged at ₹7/unit, and the remaining units are charged at ₹10/unit
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    category = "High Consumption"

print("Units Consumed:", units)
print("Total Bill: ₹", bill)
print("Category:", category)