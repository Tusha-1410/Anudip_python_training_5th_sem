# Bus Route Monitoring System

# Passenger count at each stop
passengers = [12, 18, 25, 30, 28, 15, 8]

# ----------------------------------------
# Task 1: Find the Busiest Stop

# Assume first stop is the busiest
highest_passengers = passengers[0]
busiest_stop = 1

# Compare passenger count at each stop
for i in range(len(passengers)):

    if passengers[i] > highest_passengers:
        highest_passengers = passengers[i]
        busiest_stop = i + 1   # Stop numbers start from 1

print("Busiest Stop :", busiest_stop)
print("Passengers   :", highest_passengers)

print("-" * 40)

# ----------------------------------------
# Task 2: Display Stops with Fewer Than 10 Passengers

print("Stops with Fewer Than 10 Passengers:")

for i in range(len(passengers)):

    if passengers[i] < 10:
        print("Stop", i + 1, "-", passengers[i], "passengers")

print("-" * 40)

# ----------------------------------------
# Task 3: Calculate Average Passengers

total = 0

# Add passengers from all stops
for count in passengers:
    total += count

average = total / len(passengers)

print("Average Passengers:", average)

print("-" * 40)

# ----------------------------------------
# Task 4: Check Whether Any Stop Exceeded 25 Passengers

exceeded = False

for count in passengers:

    if count > 25:
        exceeded = True
        break

if exceeded:
    print("Yes, at least one stop exceeded 25 passengers.")
else:
    print("No stop exceeded 25 passengers.")

print("-" * 40)
