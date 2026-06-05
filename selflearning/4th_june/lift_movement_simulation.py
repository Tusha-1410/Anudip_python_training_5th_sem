# Initialize lift position and distance tracker
current_floor = 0         # Starting floor of the lift (ground floor)
total_travelled = 0       # Cumulative floors travelled by the lift

# Continuous loop to process multiple lift movements until user terminates
while True:
    destination = int(input("Enter Destination Floor (-1 to stop): "))

    # Exit condition: -1 signals the end of lift movements
    if destination == -1:
        break

    # Validation: floor number cannot be negative
    if destination < 0:
        print("Invalid Floor! Enter a floor number greater than or equal to 0.")
        continue

    # Calculate floors travelled as absolute distance from current to destination
    travelled = abs(destination - current_floor)

    # Display the distance travelled for this movement
    print("Travelled:", travelled, "floors")

    # Update total distance and current floor position
    total_travelled += travelled
    current_floor = destination

# Print the cumulative distance travelled by the lift
print("\nTotal Travelled:", total_travelled, "floors")
