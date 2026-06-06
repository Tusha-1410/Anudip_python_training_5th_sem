# E-Commerce Order Analysis Using Tuple

# Each order contains:
# Product Name and Product Price

orders = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Pen Drive", 600)
]

# ----------------------------------------
# Task 1: Display products costing more than ₹1000

print("Products Costing More Than ₹1000:")

for order in orders:
    # order[1] contains product price
    if order[1] > 1000:
        print(order[0], "₹" + str(order[1]))

print("-" * 40)

# ----------------------------------------
# Task 2: Find the most expensive product

# Assume first product is the most expensive
most_expensive = orders[0]

# Compare each product price with current highest price
for order in orders:
    if order[1] > most_expensive[1]:
        most_expensive = order

print("Most Expensive Product:")
print(most_expensive[0], "₹" + str(most_expensive[1]))

print("-" * 40)

# ----------------------------------------
# Task 3: Calculate total order value

total_value = 0

# Add all product prices
for order in orders:
    total_value += order[1]

print("Total Order Value: ₹", total_value)

print("-" * 40)

# ----------------------------------------
# Task 4: Count products costing below ₹1000

count = 0

for order in orders:
    if order[1] < 1000:
        count += 1

print("Products Costing Below ₹1000:", count)

print("-" * 40)
