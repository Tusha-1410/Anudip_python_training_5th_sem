n = int(input("Enter the number of elements: "))

# Validate the count of elements
if n <= 0:
    print("Invalid Input! Enter a positive number of elements.")
else:
    # Initialize lengths: current contiguous increasing sequence and max found
    current_length = 1
    max_length = 1

    # Read the first element to initialize comparison
    prev = int(input("Enter element 1: "))

    # Read remaining elements one by one and update sequence lengths
    for i in range(2, n + 1):
        num = int(input(f"Enter element {i}: "))

        # If current number is greater than previous, increasing sequence continues
        if num > prev:
            current_length += 1
        else:
            # Sequence broke; reset current length to 1 (the current element)
            current_length = 1

        # Update maximum if current sequence is longer
        if current_length > max_length:
            max_length = current_length

        # Move window forward
        prev = num

    # Print the length of the longest continuous increasing subsequence
    print("Longest Sequence Length =", max_length)
    