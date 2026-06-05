n = int(input("Enter the number of racers: "))

# Validation: number of racers must be positive
if n <= 0:
    print("Invalid Input! Number of racers must be positive.")
else:
    # Initialize fastest and slowest trackers
    # fastest_time starts very large so any real lap time will be smaller
    fastest_time = float('inf')
    # slowest_time starts very small so any real lap time will be larger
    slowest_time = float('-inf')
    fastest_pos = 0  # position (index) of the fastest racer
    slowest_pos = 0  # position (index) of the slowest racer

    # Read lap times for each racer and update trackers
    for i in range(1, n + 1):
        lap_time = float(input(f"Enter lap time of Racer {i}: "))

        # Validate each lap time must be positive
        if lap_time <= 0:
            print("Invalid Input! Lap time must be positive.")
            exit()

        # Update fastest if current lap time is lower
        if lap_time < fastest_time:
            fastest_time = lap_time
            fastest_pos = i

        # Update slowest if current lap time is higher
        if lap_time > slowest_time:
            slowest_time = lap_time
            slowest_pos = i

    # Compute difference between slowest and fastest times
    difference = slowest_time - fastest_time

    # Print results: positions are 1-based as entered
    print("Fastest Racer Position =", fastest_pos)
    print("Slowest Racer Position =", slowest_pos)
    print("Difference =", difference)
    