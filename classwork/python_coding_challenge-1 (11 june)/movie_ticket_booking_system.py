#movie ticket booking system
tickets = {     "A1": "Booked",
                "A2": "Available",
                "A3": "Booked",
                "A4": "Available", 
                "B1": "Booked",     
                "B2": "Available",     
                "B3": "Booked",     
                "B4": "Available",     
                "C1": "Booked",     
                "C2": "Available" } 

#display available seats
print("Available seats:")
for seat, status in tickets.items():
    if status == "Available":
        print(seat)
        
#count booked and available seats
booked_count = 0
available_count = 0
for status in tickets.values():
    if status == "Booked":
        booked_count += 1
    else:
        available_count += 1

print(f"Booked seats: {booked_count}")
print(f"Available seats: {available_count}")

#reserve the first available seat
for seat, status in tickets.items():
    if status == "Available":
        #reserving the first available seat
        tickets[seat] = "Booked"
        print(f"Seat {seat} has been reserved.")
        break

#Save updated booking details to tickets.txt. 
with open("tickets.txt", "w") as file:
    for seat, status in tickets.items():
        file.write(f"Seat {seat}: {status}\n")
print("Updated booking details have been saved to tickets.txt")

#calculate occupancy percentage
total_seats = len(tickets)
occupied_seats = booked_count
occupancy_percentage = (occupied_seats / total_seats) * 100
print(f"Occupancy Percentage: {occupancy_percentage}%")

