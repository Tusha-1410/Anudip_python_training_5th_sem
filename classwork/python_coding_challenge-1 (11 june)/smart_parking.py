# Smart Parking Management System

# ----------------------------------------
# Sample Parking Data
# ----------------------------------------

parking_slots = [
    "Occupied", "Vacant", "Occupied", "Vacant",
    "Occupied", "Occupied", "Vacant", "Occupied",
    "Vacant", "Occupied"
]

# ----------------------------------------
# Task 1: Display Vacant Parking Slot Numbers
# ----------------------------------------

print("Vacant Parking Slots:")

for i in range(len(parking_slots)):

    if parking_slots[i] == "Vacant":

        # +1 because slot numbering starts from 1
        print(i + 1, end=" ")

print()

# ----------------------------------------
# Task 2: Count Occupied and Vacant Slots
# ----------------------------------------

occupied_count = 0
vacant_count = 0

for slot in parking_slots:

    if slot == "Occupied":
        occupied_count += 1

    else:
        vacant_count += 1

print("\nOccupied Slots:", occupied_count)
print("Vacant Slots:", vacant_count)

# ----------------------------------------
# Task 3: Allocate First Vacant Slot
# ----------------------------------------

allocated = False

for i in range(len(parking_slots)):

    if parking_slots[i] == "Vacant":

        parking_slots[i] = "Occupied"

        print("\nVehicle Allocated to Slot", i + 1)

        allocated = True

        break

if allocated == False:

    print("\nNo Vacant Slot Available")

# ----------------------------------------
# Task 4: Calculate Occupancy Percentage
# ----------------------------------------

occupied_slots = 0

for slot in parking_slots:

    if slot == "Occupied":
        occupied_slots += 1

total_slots = len(parking_slots)

occupancy_percentage = (occupied_slots / total_slots) * 100

print("Occupancy Percentage:", occupancy_percentage, "%")

# ----------------------------------------
# Task 5: Save Updated Parking Information
# ----------------------------------------

file = open("parking.txt", "w")

slot_number = 1

for slot in parking_slots:

    line = "Slot " + str(slot_number) + " : " + slot

    file.write(line + "\n")

    slot_number += 1

file.close()

print("Parking Details Saved Successfully.")
