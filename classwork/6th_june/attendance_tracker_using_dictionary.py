# Attendance Tracker Using Dictionary

# Dictionary to store:
# Roll Number -> Attendance Status
attendance = {}

# ----------------------------------------
# Input attendance of 30 students

for i in range(1, 31):

    # Input roll number
    roll_no = int(input(f"Enter Roll Number of Student {i}: "))

    # Validate attendance status
    while True:

        status = input("Enter Attendance (P/A): ").upper()

        if status == "P" or status == "A":

            # Store data in dictionary
            attendance[roll_no] = status
            break

        else:
            print("Invalid Input! Enter P for Present or A for Absent.")

print("-" * 40)

# ----------------------------------------
# Display complete attendance record

print("Attendance Records:")

for roll_no in attendance:

    print("Roll Number :", roll_no)
    print("Status      :", attendance[roll_no])
    print("-" * 20)

# ----------------------------------------
# Display roll numbers of present students

print("\nRoll Numbers of Present Students:")

for roll_no in attendance:

    if attendance[roll_no] == "P":
        print(roll_no)

print("-" * 40)
