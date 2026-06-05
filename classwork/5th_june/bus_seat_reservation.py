# Seat occupancy status: 1 means booked, 0 means available
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

# Initialize counters and lists for seat status
booked = 0
available = 0
available_seats = []
first_available = -1

# Count booked and available seats, and record available seat numbers
for i in range(len(seats)):
    if seats[i] == 1:
        booked += 1
    else:
        available += 1
        available_seats.append(i + 1)

# Find the first available seat number (1-indexed)
for i in range(len(seats)):
    if seats[i] == 0:
        first_available = i + 1
        break

# Calculate bus occupancy percentage
occupancy = (booked / len(seats)) * 100

# Print the seat analysis results
print("Booked Seats:", booked)
print("Available Seats:", available)
print("First Available Seat:", first_available)
print("Available Seat Numbers:", available_seats)
print("Bus Occupancy:", occupancy, "%")

# Print occupancy status depending on whether more than 70% seats are filled
if occupancy > 70:
    print("Status: More Than 70% Occupied")
else:
    print("Status: Not More Than 70% Occupied")
    