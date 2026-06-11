# --------------------------------------------------
# Smart Water Consumption Monitoring System
# --------------------------------------------------

# Dictionary storing water consumption of households
water_usage = {
    "House101": 1800,
    "House102": 2200,
    "House103": 3500,
    "House104": 2800,
    "House105": 1600,
    "House106": 4100,
    "House107": 2400,
    "House108": 3900,
    "House109": 1500,
    "House110": 4500
}

# --------------------------------------------------
# Task 1 : Display Houses Consuming More Than 3000 Litres
# --------------------------------------------------

print("Houses Consuming More Than 3000 Litres:")

for house in water_usage:

    if water_usage[house] > 3000:

        print(house)

# --------------------------------------------------
# Task 2 : Find Highest and Lowest Consumers
# --------------------------------------------------

highest_house = list(water_usage.keys())[0]
lowest_house = list(water_usage.keys())[0]

for house in water_usage:

    if water_usage[house] > water_usage[highest_house]:

        highest_house = house

    if water_usage[house] < water_usage[lowest_house]:

        lowest_house = house

print("\nHighest Consumption:",
      highest_house,
      "(" + str(water_usage[highest_house]) + " litres)")

print("Lowest Consumption:",
      lowest_house,
      "(" + str(water_usage[lowest_house]) + " litres)")

# --------------------------------------------------
# Task 3 : Calculate Total Water Consumption
# --------------------------------------------------

total_consumption = 0

for house in water_usage:

    total_consumption += water_usage[house]

print("\nTotal Consumption:",
      total_consumption,
      "litres")

# --------------------------------------------------
# Task 4 : Categorize Houses
# --------------------------------------------------

low = []
medium = []
high = []

for house in water_usage:

    usage = water_usage[house]

    if usage < 2000:

        low.append(house)

    elif usage <= 3500:

        medium.append(house)

    else:

        high.append(house)

print("\nLow Consumption:", low)
print("Medium Consumption:", medium)
print("High Consumption:", high)

# --------------------------------------------------
# Task 5 : Conservation Awareness Program
# Houses consuming more than 2500 litres
# --------------------------------------------------

eligible_count = 0

for house in water_usage:

    if water_usage[house] > 2500:

        eligible_count += 1

print("\nEligible Households:", eligible_count)
