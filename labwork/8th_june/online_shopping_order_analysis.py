# Online Shopping Order Analytics

# Dictionary containing product names and sales count
sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

# ----------------------------------
# Task 1: Display products sold more than 20 times

print("Products Sold More Than 20 Times:")

for product in sales:
    if sales[product] > 20:
        print(product)

# ----------------------------------
# Task 2: Find the best-selling product

best_product = ""
highest_sales = 0

for product in sales:
    if sales[product] > highest_sales:
        highest_sales = sales[product]
        best_product = product

print("\nBest Selling Product:")
print(best_product, "(", highest_sales, ")")

# ----------------------------------
# Task 3: Find the least-selling product

least_product = ""
lowest_sales = 9999

for product in sales:
    if sales[product] < lowest_sales:
        lowest_sales = sales[product]
        least_product = product

print("\nLeast Selling Product:")
print(least_product, "(", lowest_sales, ")")

# ----------------------------------
# Task 4: Calculate total products sold

total_sales = 0

for product in sales:
    total_sales += sales[product]

print("\nTotal Units Sold:", total_sales)

# ----------------------------------
# Task 5: Create a list of products requiring promotion

promotion_list = []

for product in sales:
    if sales[product] < 15:
        promotion_list.append(product)

print("\nProducts Requiring Promotion:")
print(promotion_list)

# ----------------------------------
# Task 6: Count products having sales between 10 and 30

count = 0

for product in sales:
    if sales[product] >= 10 and sales[product] <= 30:
        count += 1

print("\nProducts Having Sales Between 10 and 30:", count)
