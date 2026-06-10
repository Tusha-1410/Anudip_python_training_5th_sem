# Railway Reservation Seat Analyzer

# List representing seat status in a railway coach
seats = [
    "Booked", "Available", "Booked", "Booked",
    "Available", "Available", "Booked", "Available",
    "Booked", "Booked", "Available", "Booked"
]

# ---------------------------------------------------
# Function 1: Count booked and available seats
def count_seats(seats):

    booked = 0
    available = 0

    # Check each seat
    for seat in seats:

        if seat == "Booked":
            booked += 1
        else:
            available += 1

    return booked, available
# ---------------------------------------------------
# Function 2: Find the first available seat

def first_available(seats):

    # Loop through all seats
    for i in range(len(seats)):

        if seats[i] == "Available":

            # Seat number starts from 1, not 0
            return i + 1

    return "No Available Seat"


# ---------------------------------------------------
# Function 3: Calculate occupancy percentage

def occupancy_percentage(seats):

    booked = 0

    # Count booked seats
    for seat in seats:

        if seat == "Booked":
            booked += 1

    total_seats = len(seats)

    percentage = (booked / total_seats) * 100

    return percentage


# ---------------------------------------------------
# Function 4: Display all available seat numbers

def display_available_seats(seats):

    print("Available Seat Numbers:", end=" ")

    # Check each seat
    for i in range(len(seats)):
        if seats[i] == "Available":
            #i starts from 0, seat numbers start from 1
            print(i + 1, end=" ")

    print()


# ---------------------------------------------------
# Main Program

booked, available = count_seats(seats)

print("Booked Seats:", booked)
print("Available Seats:", available)

print("\nFirst Available Seat:", first_available(seats))

print("\nOccupancy Percentage:",
      round(occupancy_percentage(seats), 2), "%")

display_available_seats(seats)




