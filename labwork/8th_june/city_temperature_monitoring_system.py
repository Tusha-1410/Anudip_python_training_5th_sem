# City Temperature Monitoring System

# Dictionary containing city names and temperatures
temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

# ----------------------------------
# Task 1: Display cities having temperature above 40°C

print("Cities Above 40°C:")

for city in temperature:
    if temperature[city] > 40:
        print(city)

# ----------------------------------
# Task 2: Find the hottest city

hottest_city = ""
highest_temp = 0

for city in temperature:
    if temperature[city] > highest_temp:
        highest_temp = temperature[city]
        hottest_city = city

print("\nHottest City:")
print(hottest_city, "(", highest_temp, "°C )")

# ----------------------------------
# Task 3: Find the coolest city

coolest_city = ""
lowest_temp = 999

for city in temperature:
    if temperature[city] < lowest_temp:
        lowest_temp = temperature[city]
        coolest_city = city

print("\nCoolest City:")
print(coolest_city, "(", lowest_temp, "°C )")

# ----------------------------------
# Task 4: Calculate average temperature

total_temp = 0

for city in temperature:
    total_temp += temperature[city]

average_temp = total_temp / len(temperature)

print("\nAverage Temperature:", average_temp, "°C")

# ----------------------------------
# Task 5: Create a list of pleasant cities

pleasant_cities = []

for city in temperature:
    if temperature[city] < 35:
        pleasant_cities.append(city)

print("\nPleasant Cities:")
print(pleasant_cities)

# ----------------------------------
# Task 6: Count cities with temperature between 35°C and 40°C

count = 0

for city in temperature:
    if temperature[city] >= 35 and temperature[city] <= 40:
        count += 1

print("\nCities Between 35°C and 40°C:", count)
