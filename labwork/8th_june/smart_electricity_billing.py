# Smart Electricity Billing System

# Dictionary containing house numbers and electricity consumption
units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

# ----------------------------------
# Task 1: Display houses consuming more than 400 units

print("Houses Consuming More Than 400 Units:")

for house in units:
    if units[house] > 400:
        print(house)

# ----------------------------------
# Task 2: Find the highest-consuming house

highest_house = ""
highest_units = 0

for house in units:
    if units[house] > highest_units:
        highest_units = units[house]
        highest_house = house

print("\nHighest Consumption:")
print(highest_house, "(", highest_units, "units )")

# ----------------------------------
# Task 3: Find the lowest-consuming house

lowest_house = ""
lowest_units = 9999

for house in units:
    if units[house] < lowest_units:
        lowest_units = units[house]
        lowest_house = house

print("\nLowest Consumption:")
print(lowest_house, "(", lowest_units, "units )")

# ----------------------------------
# Task 4: Calculate total units consumed

total_units = 0

for house in units:
    total_units += units[house]

print("\nTotal Units Consumed:", total_units)

# ----------------------------------
# Task 5: Create lists based on consumption

low_consumption = []
medium_consumption = []
high_consumption = []

for house in units:

    if units[house] < 200:
        low_consumption.append(house)

    elif units[house] <= 400:
        medium_consumption.append(house)

    else:
        high_consumption.append(house)

print("\nLow Consumption:", low_consumption)
print("Medium Consumption:", medium_consumption)
print("High Consumption:", high_consumption)

# ----------------------------------
# Task 6: Count houses eligible for energy-saving campaign

count = 0

for house in units:
    if units[house] > 300:
        count += 1

print("\nEligible for Energy-Saving Campaign:", count)
