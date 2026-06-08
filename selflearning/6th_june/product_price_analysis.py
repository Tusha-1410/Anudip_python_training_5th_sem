# Product Price Analysis

# Dictionary containing product names and their prices
prices = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1800,
    "Monitor": 12000,
    "Printer": 9000,
    "Tablet": 28000,
    "Speaker": 3500,
    "Webcam": 2500,
    "Headphones": 4200,
    "Router": 3200
}

# ----------------------------------
# Task 1: Display products costing more than ₹5000

print("Products Costing More Than ₹5000:")

for product in prices:
    if prices[product] > 5000:
        print(product, "-", prices[product])

# ----------------------------------
# Task 2: Count products costing less than ₹3000

count = 0

for product in prices:
    if prices[product] < 3000:
        count += 1

print("\nNumber of Products Costing Less Than ₹3000:", count)

# ----------------------------------
# Task 3: Find the most expensive product

expensive_product = ""
highest_price = 0

for product in prices:
    if prices[product] > highest_price:
        highest_price = prices[product]
        expensive_product = product

print("\nMost Expensive Product:")
print(expensive_product, "-", highest_price)

# ----------------------------------
# Task 4: Create a list of products priced between ₹2000 and ₹10000

product_list = []

for product in prices:
    if prices[product] >= 2000 and prices[product] <= 10000:
        product_list.append(product)

print("\nProducts Priced Between ₹2000 and ₹10000:")
print(product_list)

# ----------------------------------
# Task 5: Calculate the total value of all products

total_value = 0

for product in prices:
    total_value += prices[product]

print("\nTotal Value of All Products:", total_value)

