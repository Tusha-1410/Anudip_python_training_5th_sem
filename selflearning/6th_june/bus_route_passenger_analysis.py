# Bus Route Passenger Analysis

# Dictionary containing bus stops and number of passengers
passengers = {
    "Stop1": 12,
    "Stop2": 25,
    "Stop3": 18,
    "Stop4": 32,
    "Stop5": 9,
    "Stop6": 28,
    "Stop7": 14,
    "Stop8": 7,
    "Stop9": 21,
    "Stop10": 16
}

# ----------------------------------
# Task 1: Display stops having more than 20 passengers

print("Stops Having More Than 20 Passengers:")

for stop in passengers:
    if passengers[stop] > 20:
        print(stop, "-", passengers[stop])

# ----------------------------------
# Task 2: Count stops with fewer than 10 passengers

count = 0

for stop in passengers:
    if passengers[stop] < 10:
        count += 1

print("\nStops with Fewer Than 10 Passengers:", count)

# ----------------------------------
# Task 3: Find the busiest stop

busiest_stop = ""
max_passengers = 0

for stop in passengers:
    if passengers[stop] > max_passengers:
        max_passengers = passengers[stop]
        busiest_stop = stop

print("\nBusiest Stop:")
print(busiest_stop, "-", max_passengers)

# ----------------------------------
# Task 4: Create a list of stops requiring an extra bus

extra_bus_stops = []

for stop in passengers:
    if passengers[stop] > 25:
        extra_bus_stops.append(stop)

print("\nStops Requiring an Extra Bus:")
print(extra_bus_stops)

# ----------------------------------
# Task 5: Calculate the average number of passengers

total_passengers = 0

for stop in passengers:
    total_passengers += passengers[stop]

average_passengers = total_passengers / len(passengers)

print("\nAverage Number of Passengers:", average_passengers)
