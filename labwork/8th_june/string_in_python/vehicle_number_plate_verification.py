# Vehicle Number Plate Verification

# Taking vehicle number as input
vehicle_no = input("Enter Vehicle Number: ")

# ----------------------------------
# Task 1: Extract state code

state_code = vehicle_no[0:2]

print("\nState Code:", state_code)

# ----------------------------------
# Task 2: Extract district code

district_code = vehicle_no[2:4]

print("District Code:", district_code)

# ----------------------------------
# Task 3: Extract vehicle series

series = vehicle_no[4:6]

print("Series:", series)

# ----------------------------------
# Task 4: Extract vehicle number

number = vehicle_no[6:10]

print("Vehicle Number:", number)

# ----------------------------------
# Task 5: Count letters and digits

letter_count = 0
digit_count = 0

for ch in vehicle_no:

    if ch.isalpha():
        letter_count += 1

    elif ch.isdigit():
        digit_count += 1

print("\nTotal Letters:", letter_count)
print("Total Digits:", digit_count)

# ----------------------------------
# Task 6: Verify vehicle number format

part1 = vehicle_no[0:2].isalpha()   # First 2 letters
part2 = vehicle_no[2:4].isdigit()   # Next 2 digits
part3 = vehicle_no[4:6].isalpha()   # Next 2 letters
part4 = vehicle_no[6:10].isdigit()  # Last 4 digits

# ----------------------------------
# Task 7: Display validity

if len(vehicle_no) == 10 and part1 and part2 and part3 and part4:
    print("\nVehicle Number Status: Valid")
else:
    print("\nVehicle Number Status: Invalid")
    