# Electricity Consumption Report

# Dictionary containing house numbers and electricity consumption
units = {
    "House101": 320,
    "House102": 180,
    "House103": 450,
    "House104": 290,
    "House105": 150,
    "House106": 510,
    "House107": 220,
    "House108": 390,
    "House109": 170,
    "House110": 260
}

# ----------------------------------
# Task 1: Display houses consuming more than 300 units

print("Houses Consuming More Than 300 Units:")

for house in units:
    if units[house] > 300:
        print(house, "-", units[house])

# ----------------------------------
# Task 2: Count houses consuming less than 200 units

count = 0

for house in units:
    if units[house] < 200:
        count += 1

print("\nHouses Consuming Less Than 200 Units:", count)

# ----------------------------------
# Task 3: Find the house with the highest consumption

highest_house = ""
highest_units = 0

for house in units:
    if units[house] > highest_units:
        highest_units = units[house]
        highest_house = house

print("\nHouse with Highest Consumption:")
print(highest_house, "-", highest_units)

# ----------------------------------
# Task 4: Create a list of houses eligible for awareness campaign

campaign_list = []

for house in units:
    if units[house] > 400:
        campaign_list.append(house)

print("\nHouses Eligible for Energy-Saving Awareness Campaign:")
print(campaign_list)

# ----------------------------------
# Task 5: Categorize houses

print("\nHouse Categories:")

for house in units:

    if units[house] < 200:
        category = "Low"

    elif units[house] <= 350:
        category = "Medium"

    else:
        category = "High"

    print(house, "-", units[house], "Units -", category)
    