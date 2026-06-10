# E-Commerce Inventory & Sales Dashboard

products = {
    "P101": {"name": "Laptop", "price": 55000, "stock": 12, "sold": 25},
    "P102": {"name": "Mouse", "price": 500, "stock": 20, "sold": 50},
    "P103": {"name": "Keyboard", "price": 1200, "stock": 8, "sold": 30},
    "P104": {"name": "Monitor", "price": 12000, "stock": 4, "sold": 15},
    "P105": {"name": "Printer", "price": 8500, "stock": 0, "sold": 10},
    "P106": {"name": "Scanner", "price": 6500, "stock": 3, "sold": 8},
    "P107": {"name": "Speaker", "price": 2500, "stock": 15, "sold": 18},
    "P108": {"name": "Webcam", "price": 1800, "stock": 6, "sold": 12},
    "P109": {"name": "Headphone", "price": 2200, "stock": 10, "sold": 35},
    "P110": {"name": "Pendrive", "price": 700, "stock": 25, "sold": 60},
    "P111": {"name": "SSD", "price": 5000, "stock": 7, "sold": 22},
    "P112": {"name": "Hard Disk", "price": 4500, "stock": 9, "sold": 17},
    "P113": {"name": "RAM", "price": 3000, "stock": 11, "sold": 28},
    "P114": {"name": "Graphics Card", "price": 25000, "stock": 2, "sold": 5},
    "P115": {"name": "Processor", "price": 18000, "stock": 5, "sold": 9},
    "P116": {"name": "Motherboard", "price": 9000, "stock": 4, "sold": 14},
    "P117": {"name": "Cabinet", "price": 3500, "stock": 8, "sold": 11},
    "P118": {"name": "UPS", "price": 4000, "stock": 3, "sold": 7},
    "P119": {"name": "Projector", "price": 30000, "stock": 1, "sold": 4},
    "P120": {"name": "Router", "price": 2500, "stock": 13, "sold": 20},
    "P121": {"name": "Switch", "price": 2000, "stock": 6, "sold": 13},
    "P122": {"name": "Modem", "price": 1800, "stock": 2, "sold": 6},
    "P123": {"name": "Tablet", "price": 15000, "stock": 5, "sold": 16},
    "P124": {"name": "Smartphone", "price": 22000, "stock": 7, "sold": 40},
    "P125": {"name": "Smartwatch", "price": 5000, "stock": 4, "sold": 19},
    "P126": {"name": "Power Bank", "price": 1500, "stock": 12, "sold": 27},
    "P127": {"name": "Charger", "price": 800, "stock": 18, "sold": 33},
    "P128": {"name": "Microphone", "price": 3000, "stock": 3, "sold": 8},
    "P129": {"name": "Camera", "price": 45000, "stock": 2, "sold": 3},
    "P130": {"name": "Drone", "price": 60000, "stock": 1, "sold": 2}
}

# 1. Display all products
print("\nALL PRODUCTS")
for pid in products:
    print(pid, products[pid])

# 2. Add a new product
pid = input("\nEnter Product ID: ")
name = input("Enter Product Name: ")
price = int(input("Enter Price: "))
stock = int(input("Enter Stock: "))
sold = int(input("Enter Sold Quantity: "))

products[pid] = {
    "name": name,
    "price": price,
    "stock": stock,
    "sold": sold
}

print("Product Added Successfully")

# 3. Update stock after sales
pid = input("\nEnter Product ID: ")

if pid in products:
    qty = int(input("Enter Quantity Sold: "))

    if qty <= products[pid]["stock"]:
        products[pid]["stock"] -= qty
        products[pid]["sold"] += qty
        print("Stock Updated")
    else:
        print("Not Enough Stock")
else:
    print("Product Not Found")

# 4. Out-of-stock products
print("\nOUT OF STOCK PRODUCTS")

for pid in products:
    if products[pid]["stock"] == 0:
        print(pid, products[pid]["name"])

# 5. Products with stock less than 5
print("\nLOW STOCK PRODUCTS")

for pid in products:
    if products[pid]["stock"] < 5:
        print(pid, products[pid]["name"], products[pid]["stock"])

# 6. Total inventory value
inventory_value = 0

for pid in products:
    inventory_value += (
        products[pid]["price"] *
        products[pid]["stock"]
    )

print("\nTotal Inventory Value =", inventory_value)

# 7. Best-selling product
first = True

for pid in products:

    if first:
        best = pid
        first = False

    elif products[pid]["sold"] > products[best]["sold"]:
        best = pid

print("\nBest Selling Product")
print(best, products[best])

# 8. Least-selling product
first = True

for pid in products:

    if first:
        least = pid
        first = False

    elif products[pid]["sold"] < products[least]["sold"]:
        least = pid

print("\nLeast Selling Product")
print(least, products[least])

# 9. Total revenue generated
revenue = 0

for pid in products:
    revenue += (
        products[pid]["price"] *
        products[pid]["sold"]
    )

print("\nTotal Revenue =", revenue)

# 10. Low-stock report
print("\nLOW STOCK REPORT")

for pid in products:

    if products[pid]["stock"] < 5:
        print(pid,
              products[pid]["name"],
              "Stock:",
              products[pid]["stock"])

# 11. Products whose sales exceed average sales
total_sales = 0

for pid in products:
    total_sales += products[pid]["sold"]

avg_sales = total_sales / len(products)

print("\nPRODUCTS ABOVE AVERAGE SALES")

for pid in products:

    if products[pid]["sold"] > avg_sales:
        print(pid,
              products[pid]["name"],
              products[pid]["sold"])

# 12. Promotion Products (sales < 10)
promotion = {}

for pid in products:

    if products[pid]["sold"] < 10:
        promotion[pid] = products[pid]

print("\nPROMOTION PRODUCTS")

for pid in promotion:
    print(pid, promotion[pid])

# CHALLENGE: Complete Business Report

print("\n========== BUSINESS REPORT ==========")

print("Total Products =", len(products))
print("Total Inventory Value =", inventory_value)
print("Total Revenue =", revenue)

print("\nBest Selling Product:")
print(best, products[best]["name"])

print("\nLeast Selling Product:")
print(least, products[least]["name"])

low_stock_count = 0

for pid in products:
    if products[pid]["stock"] < 5:
        low_stock_count += 1

print("\nLow Stock Products =", low_stock_count)

print("Promotion Eligible Products =", len(promotion))
