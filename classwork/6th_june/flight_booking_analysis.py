# Flight Booking Analysis Using Tuples

# Each booking is represented as a tuple of (passenger_id, destination, status).
bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

# ----------------------------------------
# Task 1: Display all confirmed passengers
# Iterate through each booking and print details only if the status is Confirmed.
print("Confirmed Passengers:")
for booking in bookings:
    if booking[2] == "Confirmed":
        print(booking[0], booking[1])

print("-" * 40)

# ----------------------------------------
# Task 2: Count passengers travelling to Delhi
# Use a counter to tally bookings where the destination is Delhi.
delhi_count = 0
for booking in bookings:
    if booking[1] == "Delhi":
        delhi_count += 1
print("Passengers Travelling to Delhi:", delhi_count)

print("-" * 40)

# ----------------------------------------
# Task 3: Count Confirmed, Waiting and Cancelled bookings
# Track the number of bookings in each status category.
confirmed = 0
waiting = 0
cancelled = 0
for booking in bookings:
    if booking[2] == "Confirmed":
        confirmed += 1
    elif booking[2] == "Waiting":
        waiting += 1
    elif booking[2] == "Cancelled":
        cancelled += 1

print("Confirmed :", confirmed)
print("Waiting   :", waiting)
print("Cancelled :", cancelled)

print("-" * 40)

# ----------------------------------------
# Task 4: Create a list of passenger IDs with Waiting status
# Build a list of IDs for passengers currently on the waiting list.
waiting_list = []
for booking in bookings:
    if booking[2] == "Waiting":
        waiting_list.append(booking[0])
print("Waiting List:", waiting_list)

print("-" * 40)

# ----------------------------------------
# Task 5: Find destination with highest bookings
# Count bookings per destination and determine which destination has the highest count.
destinations = {}
for booking in bookings:
    destination = booking[1]
    if destination in destinations:
        destinations[destination] += 1
    else:
        destinations[destination] = 1

most_booked = max(destinations, key=destinations.get)
print("Most Booked Destination:", most_booked)