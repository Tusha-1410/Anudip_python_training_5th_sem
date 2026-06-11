#smart railway reservation system
seats = {   1: "Booked", 
            2: "Available", 
            3: "Booked", 
            4: "Available",
            5: "Booked", 
            6: "Booked",   
            7: "Available",
            8: "Booked",
            9: "Available",
            10: "Booked" } 

#display all available seat number

print("Available seats:")
for seat, status in seats.items():
    if status == "Available":
        print(seat)

#count booked and available seats
booked_count = 0
available_count = 0
for status in seats.values():
    if status == "Booked":
        booked_count += 1
    else:
        available_count += 1
print("\nTotal Booked Seats:", booked_count)
print("Total Available Seats:", available_count) 

#reserve the first available seat
for seat, status in seats.items():
    if status == "Available":
        #reserving the first available seat
        seats[seat] = "Booked"
        print("\nSeat", seat, "has been reserved.")
        break

#cancel booking for a given seat number
seat_to_cancel = 4
if seat_to_cancel in seats and seats[seat_to_cancel] == "Booked":
    seats[seat_to_cancel] = "Available"
    print("\nBooking for seat", seat_to_cancel, "has been cancelled.")
else:
    print("\nSeat", seat_to_cancel, "is not booked or does not exist in the system.")

#store the updated reservation status in reservations.txt file
with open("reservations.txt", "w") as file:
    for seat, status in seats.items():
        file.write(f"Seat {seat}: {status}\n")
        print("\nUpdated reservation status has been saved to reservations.txt")

#display occupancy percentage
total_seats = len(seats)
occupied_seats = booked_count
occupancy_percentage = (occupied_seats / total_seats) * 100
print("\nOccupancy Percentage: " + str(occupancy_percentage) + "%")





