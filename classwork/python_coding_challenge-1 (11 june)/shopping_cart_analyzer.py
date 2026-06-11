# --------------------------------------------------
# Online Shopping Cart Analyzer
# --------------------------------------------------

# List containing product prices
cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999]

# --------------------------------------------------
# Task 1 : Calculate Total Cart Value
# --------------------------------------------------

total = 0

for price in cart:

    total += price

print("Total Cart Value: ₹", total)

# --------------------------------------------------
# Task 2 : Find Most Expensive and Cheapest Product
# --------------------------------------------------

most_expensive = cart[0]
cheapest = cart[0]

for price in cart:

    if price > most_expensive:
        # updating most expensive price
        most_expensive = price

    if price < cheapest:

        cheapest = price

print("Most Expensive Product: ₹", most_expensive)
print("Cheapest Product: ₹", cheapest)

# --------------------------------------------------
# Task 3 : Count Premium Shipping Products
# (Price > ₹1000)
# --------------------------------------------------

premium_count = 0

for price in cart:

    if price > 1000:

        premium_count += 1

print("Premium Shipping Eligible Products:", premium_count)

# --------------------------------------------------
# Task 4 : Generate Discount Eligible Product List
# (Price > ₹1500)
# --------------------------------------------------

discount_products = []

for price in cart:

    if price > 1500:

        discount_products.append(price)

print("Discount Eligible Products:", discount_products)

# --------------------------------------------------
# Task 5 : Calculate Average Product Price
# --------------------------------------------------

average_price = total / len(cart)

print("Average Product Price: ₹", average_price)

