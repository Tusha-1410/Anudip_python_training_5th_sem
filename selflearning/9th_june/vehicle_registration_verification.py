# --------------------------------------------------
# Vehicle Registration Verification System
# --------------------------------------------------

# List containing 20 vehicle registration numbers

vehicles = [
    "MH12AB4589",
    "DL05XY9988",
    "KA03PQ1234",
    "UP14CD5678",
    "MH20EF2345",
    "DL11GH8765",
    "KA09IJ4567",
    "UP32KL9876",
    "MH18MN1111",
    "DL22OP2222",
    "KA07QR3333",
    "UP40ST4444",
    "MH15UV5555",
    "DL08WX6666",
    "KA12YZ7777",
    "UP21AB8888",
    "MH10CD9999",
    "KA05EF1212",
    "UP09GH3434",
    "XX123456"          # Invalid Registration
]

# Dictionary to count vehicles state-wise

state_count = {}

# List to store invalid registrations

invalid_registrations = []

# --------------------------------------------------
# Analyze each registration number

for vehicle in vehicles:

    print("\n================================")
    print("Vehicle Number :", vehicle)

    # ------------------------------------------
    # Extract different parts

    if len(vehicle) >= 10:

        state_code = vehicle[0:2]
        district_code = vehicle[2:4]
        series = vehicle[4:6]
        vehicle_number = vehicle[6:]

        print("State Code    :", state_code)
        print("District Code :", district_code)
        print("Series        :", series)
        print("Vehicle Number:", vehicle_number)

    # ------------------------------------------
    # Count letters and digits

    letters = 0
    digits = 0

    for ch in vehicle:

        if ch.isalpha():
            letters += 1

        elif ch.isdigit():
            digits += 1

    print("Letters :", letters)
    print("Digits  :", digits)

    # ------------------------------------------
    # Validate Registration Format

    valid = True

    if len(vehicle) != 10:
        valid = False

    elif not vehicle[0:2].isalpha():
        valid = False

    elif not vehicle[2:4].isdigit():
        valid = False

    elif not vehicle[4:6].isalpha():
        valid = False

    elif not vehicle[6:10].isdigit():
        valid = False

    # ------------------------------------------
    # Display validity status

    if valid:

        print("Status : Valid")

        # Count vehicles state-wise

        if state_code in state_count:
            state_count[state_code] += 1
        else:
            state_count[state_code] = 1

    else:

        print("Status : Invalid")

        invalid_registrations.append(vehicle)

# --------------------------------------------------
# Display Invalid Registrations

print("\n================================")
print("INVALID REGISTRATIONS")
print("================================")

for vehicle in invalid_registrations:

    print(vehicle)

# --------------------------------------------------
# State-wise Vehicle Count Report

print("\n================================")
print("STATE-WISE REPORT")
print("================================")

for state in state_count:

    print(state, "->", state_count[state], "Vehicles")
    