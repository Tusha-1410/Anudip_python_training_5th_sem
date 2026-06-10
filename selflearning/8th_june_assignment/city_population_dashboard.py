# City Population & Development Dashboard

# Dictionary of cities with population, area in square kilometers, and literacy rate.
# This dataset is used to compute population, literacy, density, and development metrics.
cities = {
    "Delhi": {"population": 32000000, "area": 1484, "literacy": 89},
    "Mumbai": {"population": 21000000, "area": 603, "literacy": 91},
    "Kolkata": {"population": 15000000, "area": 205, "literacy": 88},
    "Chennai": {"population": 11000000, "area": 426, "literacy": 90},
    "Bangalore": {"population": 14000000, "area": 709, "literacy": 92},
    "Hyderabad": {"population": 10500000, "area": 650, "literacy": 87},
    "Pune": {"population": 7500000, "area": 516, "literacy": 91},
    "Ahmedabad": {"population": 8500000, "area": 505, "literacy": 86},
    "Jaipur": {"population": 4200000, "area": 467, "literacy": 84},
    "Lucknow": {"population": 3800000, "area": 631, "literacy": 82},
    "Kanpur": {"population": 3100000, "area": 403, "literacy": 81},
    "Nagpur": {"population": 2900000, "area": 218, "literacy": 89},
    "Indore": {"population": 3300000, "area": 530, "literacy": 87},
    "Bhopal": {"population": 2500000, "area": 285, "literacy": 85},
    "Patna": {"population": 2800000, "area": 250, "literacy": 79},
    "Surat": {"population": 7000000, "area": 326, "literacy": 89},
    "Agra": {"population": 2000000, "area": 188, "literacy": 78},
    "Varanasi": {"population": 1800000, "area": 153, "literacy": 80},
    "Meerut": {"population": 1700000, "area": 141, "literacy": 77},
    "Prayagraj": {"population": 1600000, "area": 365, "literacy": 83},
    "Amritsar": {"population": 1400000, "area": 139, "literacy": 85},
    "Ludhiana": {"population": 1800000, "area": 159, "literacy": 86},
    "Jodhpur": {"population": 1500000, "area": 233, "literacy": 81},
    "Udaipur": {"population": 900000, "area": 64, "literacy": 90},
    "Dehradun": {"population": 800000, "area": 196, "literacy": 89},
    "Ranchi": {"population": 1300000, "area": 175, "literacy": 84},
    "Raipur": {"population": 1200000, "area": 226, "literacy": 86},
    "Guwahati": {"population": 1100000, "area": 328, "literacy": 88},
    "Shimla": {"population": 250000, "area": 35, "literacy": 94},
    "Panaji": {"population": 120000, "area": 36, "literacy": 95}
}

# 1. Display all city details
# Print every city and its stored development data.
print("\nALL CITY DETAILS")

for city in cities:
    print(city, cities[city])

# 2. Most Populated City
# Identify the city with the highest population total.
first = True

for city in cities:

    if first:
        most_populated = city
        first = False

    elif cities[city]["population"] > cities[most_populated]["population"]:
        most_populated = city

print("\nMost Populated City")
print(most_populated, cities[most_populated])

# 3. Least Populated City
# Identify the city with the smallest population total.
first = True

for city in cities:

    if first:
        least_populated = city
        first = False

    elif cities[city]["population"] < cities[least_populated]["population"]:
        least_populated = city

print("\nLeast Populated City")
print(least_populated, cities[least_populated])

# 4. Average Population
# Compute the mean city population for the dataset.
total_population = 0

for city in cities:
    total_population += cities[city]["population"]

average_population = total_population / len(cities)

print("\nAverage Population =", int(average_population))

# 5. Literacy Rate Above 90%
# List cities with literacy rates above 90%.
print("\nHIGH LITERACY CITIES (>90%)")

for city in cities:

    if cities[city]["literacy"] > 90:
        print(city, cities[city]["literacy"])

# 6. Literacy Below Average
# Compute average literacy and list cities below that level.
total_literacy = 0

for city in cities:
    total_literacy += cities[city]["literacy"]

average_literacy = total_literacy / len(cities)

print("\nLITERACY BELOW AVERAGE")

for city in cities:

    if cities[city]["literacy"] < average_literacy:
        print(city, cities[city]["literacy"])

# 7. Population Density
# Calculate population density for each city.
print("\nPOPULATION DENSITY")

for city in cities:

    density = cities[city]["population"] / cities[city]["area"]

    print(city, "=", round(density, 2))

# 8. City with Highest Density
# Find the city with the highest population per square kilometer.
first = True

for city in cities:

    density = cities[city]["population"] / cities[city]["area"]

    if first:
        highest_density = city
        max_density = density
        first = False

    elif density > max_density:
        max_density = density
        highest_density = city

print("\nHighest Density City")
print(highest_density, round(max_density, 2))

# 9. Categorize Cities
# Assign a size category to each city based on population.
print("\nCITY CATEGORIES")

for city in cities:

    population = cities[city]["population"]

    if population >= 10000000:
        category = "Large"

    elif population >= 2000000:
        category = "Medium"

    else:
        category = "Small"

    print(city, "-", category)

# 10. Development Priority List
# Recommend cities that may need additional development support.
print("\nDEVELOPMENT PRIORITY LIST")

for city in cities:

    if cities[city]["literacy"] < 85:
        print(city,
              "Literacy:",
              cities[city]["literacy"])

# 11. Separate Dictionaries
# Split cities into high and low literacy dictionaries.
high_literacy = {}
low_literacy = {}

for city in cities:

    if cities[city]["literacy"] >= 90:
        high_literacy[city] = cities[city]
    else:
        low_literacy[city] = cities[city]

print("\nHIGH LITERACY CITIES")
for city in high_literacy:
    print(city)

print("\nLOW LITERACY CITIES")
for city in low_literacy:
    print(city)

# 12. National Summary Report
# Print the overall city development summary.
print("\n========== NATIONAL SUMMARY REPORT ==========")

print("Total Cities =", len(cities))
print("Average Population =", int(average_population))
print("Average Literacy =", round(average_literacy, 2))

print("\nMost Populated City =", most_populated)
print("Least Populated City =", least_populated)
print("Highest Density City =", highest_density)

# Challenge: Rank Cities by Population Density
# Rank cities from highest to lowest population density.
print("\n========== CITY DENSITY RANKING ==========")

temp_cities = {}

for city in cities:
    temp_cities[city] = cities[city]

rank = 1

while len(temp_cities) > 0:

    first = True

    for city in temp_cities:

        density = (
            temp_cities[city]["population"] /
            temp_cities[city]["area"]
        )

        if first:
            top_city = city
            top_density = density
            first = False

        elif density > top_density:
            top_city = city
            top_density = density

    print(rank, ".", top_city, "-", round(top_density, 2))

    del temp_cities[top_city]

    rank += 1
