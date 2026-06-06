# Train Reservation Waiting List System

# Passenger Name and Ticket Status
passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

# ----------------------------------------
# Task 1: Display All Waiting-List Passengers

print("Waiting List Passengers:")

for passenger in passengers:

    # passenger[1] contains ticket status
    if passenger[1] == "Waiting":
        print(passenger[0])

print("-" * 40)

# ----------------------------------------
# Task 2: Count Confirmed and Waiting Passengers

confirmed = 0
waiting = 0

for passenger in passengers:

    if passenger[1] == "Confirmed":
        confirmed += 1
    else:
        waiting += 1

print("Confirmed Passengers:", confirmed)
print("Waiting Passengers  :", waiting)

print("-" * 40)

# ----------------------------------------
# Task 3: Check Whether a Specific Passenger Has a Confirmed Ticket

# Passenger to search
search_name = "Rahul"

found = False

for passenger in passengers:

    if passenger[0] == search_name:

        found = True

        if passenger[1] == "Confirmed":
            print(search_name, "has a Confirmed Ticket")
        else:
            print(search_name, "is on the Waiting List")

        break

# If passenger name is not found
if found == False:
    print("Passenger Not Found")

print("-" * 40)

# ----------------------------------------
# Task 4: Create Separate Lists for Confirmed and Waiting Passengers

confirmed_list = []
waiting_list = []

for passenger in passengers:

    if passenger[1] == "Confirmed":
        confirmed_list.append(passenger[0])
    else:
        waiting_list.append(passenger[0])

print("Confirmed Passengers List:")
print(confirmed_list)

print()

print("Waiting Passengers List:")
print(waiting_list)

print("-" * 40)
