# Inventory stock levels for each product
stock = [25, 5, 0, 12, 3, 18, 0, 30]

# Counters and lists to categorize stock status
out_of_stock = 0
restock_required = []
healthy_stock = []
available_products = 0

for qty in stock:
    # Count products that are completely out of stock
    if qty == 0:
        out_of_stock += 1

    # Track products that need restocking (less than 10 units)
    if qty < 10:
        restock_required.append(qty)

    # Count products that are currently available
    if qty > 0:
        available_products += 1

    # Track products with healthy stock levels (15 or more units)
    if qty >= 15:
        healthy_stock.append(qty)

# Print inventory analysis results
print("Out of Stock Products:", out_of_stock)
print("Restock Required:", restock_required)
print("Available Products:", available_products)
print("Healthy Stock:", healthy_stock)
