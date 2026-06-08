# Inventory Management System

# Dictionary containing product names and their stock
inventory = {
    "Notebook": 45,
    "Pen": 120,
    "Pencil": 80,
    "Eraser": 25,
    "Marker": 15,
    "Stapler": 8,
    "Glue": 12,
    "Scale": 30,
    "Folder": 5,
    "Calculator": 3
}

# ----------------------------------
# Task 1: Display products with stock less than 10

print("Products with stock less than 10:")

for product in inventory:
    if inventory[product] < 10:
        print(product, "-", inventory[product])

# ----------------------------------
# Task 2: Count products having stock more than 50

count = 0

for product in inventory:
    if inventory[product] > 50:
        count += 1

print("\nProducts with stock more than 50:", count)

# ----------------------------------
# Task 3: Find the product with minimum stock

min_product = ""
min_stock = 9999   # Assuming stock will not exceed this value

for product in inventory:
    if inventory[product] < min_stock:
        min_stock = inventory[product]
        min_product = product

print("\nProduct with Minimum Stock:")
print(min_product, "-", min_stock)

# ----------------------------------
# Task 4: Create a list of products that need restocking

restock_list = []

for product in inventory:
    if inventory[product] < 20:
        restock_list.append(product)

print("\nProducts Requiring Restocking:")
print(restock_list)

# ----------------------------------
# Task 5: Calculate total inventory count

total_stock = 0

for product in inventory:
    total_stock += inventory[product]

print("\nTotal Inventory Count:", total_stock)
