# Warehouse Product Inspection System

# Product ID and Quality Status
products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

# ----------------------------------------
# Task 1: Display Failed Product IDs

print("Failed Product IDs:")

for product in products:

    if product[1] == "Fail":
        print(product[0])

print("-" * 40)

# ----------------------------------------
# Task 2: Count Passed and Failed Products

passed = 0
failed = 0

for product in products:

    if product[1] == "Pass":
        passed += 1
    else:
        failed += 1

print("Passed Products :", passed)
print("Failed Products :", failed)

print("-" * 40)

# ----------------------------------------
# Task 3: Calculate Pass Percentage

# Formula:
# (Passed Products / Total Products) * 100

pass_percentage = (passed / len(products)) * 100

print("Pass Percentage:", pass_percentage, "%")

print("-" * 40)

# ----------------------------------------
# Task 4: Stop Checking if 3 Failures Are Found

failure_count = 0

print("Checking Products...")

for product in products:

    # Check whether the product has failed
    if product[1] == "Fail":

        failure_count += 1

        print("Failed Product Found:", product[0])

        # Stop checking when 3 failures are found
        if failure_count == 3:
            print("3 Failures Found. Inspection Stopped.")
            break

# If fewer than 3 failures exist
if failure_count < 3:
    print("Less than 3 failures found.")

print("-" * 40)
