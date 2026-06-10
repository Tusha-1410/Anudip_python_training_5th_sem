# Food Delivery Performance Tracker

# List containing delivery times (in minutes)
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# --------------------------------------------------
# Function 1: Find the fastest delivery time

def fastest_delivery(times):
    #assume the first delivery time is the fastest
    fastest = times[0]
    # Loop through all delivery times
    for time in times:
        if time < fastest:
            fastest = time
    return fastest
        
# --------------------------------------------------
# Function 2: Find delayed orders (> 45 minutes)

def delayed_orders(times):

    delayed = []

    # Check each delivery time
    for time in times:

        if time > 45:
            delayed.append(time)

    return delayed

# --------------------------------------------------
# Function 3: Calculate average delivery time

def average_delivery_times(times):

    total_time = 0

    # Sum all delivery times
    for time in times:
        total_time += time

    average = total_time / len(times)

    return average

# --------------------------------------------------
# Function 4: Calculate on-time delivery percentage (<= 45 minutes)
def delivery_category(times):

    print("\nCategories:")

    for time in times:

        # Fast Delivery
        if time <= 30:
            print(time, "-> Fast")

        # Normal Delivery
        elif time <= 45:
            print(time, "-> Normal")

        # Delayed Delivery
        else:
            print(time, "-> Delayed")

# --------------------------------------------------
# Main Program

print("Fastest Delivery:",
      fastest_delivery(delivery_time), "minutes")

print("\nDelayed Orders:",
      delayed_orders(delivery_time))

print("\nAverage Delivery Time:",
      round(average_delivery_times(delivery_time), 2),
      "minutes")

delivery_category(delivery_time)

