# Smart Parking System Analysis

# 1 = Occupied Slot
# 0 = Available Slot

slots = [1, 0, 1, 1, 0, 0, 1, 0]

# ----------------------------------------
# Task 1: Count Occupied and Available Slots

occupied = 0
available = 0

for slot in slots:

    if slot == 1:
        occupied += 1
    else:
        available += 1

print("Occupied Slots :", occupied)
print("Available Slots:", available)

print("-" * 40)

# ----------------------------------------
# Task 2: Find the First Available Slot

first_available = -1

for i in range(len(slots)):

    if slots[i] == 0:
        first_available = i + 1   # Slot numbers start from 1
        break

print("First Available Slot:", first_available)

print("-" * 40)

# ----------------------------------------
# Task 3: Display All Available Slot Numbers

print("Available Slot Numbers:")

for i in range(len(slots)):

    if slots[i] == 0:
        print("Slot", i + 1)   # Adding 1 because slot numbering starts from 1

print("-" * 40)

# ----------------------------------------
# Task 4: Check Whether Parking Occupancy Exceeds 75%

# Occupancy Percentage Formula:
# (Occupied Slots / Total Slots) * 100

occupancy_percentage = (occupied / len(slots)) * 100

print("Occupancy Percentage:", occupancy_percentage, "%")

if occupancy_percentage > 75:
    print("Parking Occupancy Exceeds 75%")
else:
    print("Parking Occupancy Does Not Exceed 75%")

print("-" * 40)
