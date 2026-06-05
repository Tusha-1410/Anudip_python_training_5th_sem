# List of numbers to check for consecutive values
numbers = [4, 5, 6, 10, 11, 15, 16, 17]

# List to store all consecutive number pairs
consecutive_pairs = []

# Iterate through the list using indexes, stopping one before the last element
for i in range(len(numbers) - 1):
    # Check if the next number is exactly one more than the current number
    if numbers[i + 1] == numbers[i] + 1:
        print(numbers[i], "and", numbers[i + 1], "are consecutive")

        # Save the consecutive pair as a tuple
        consecutive_pairs.append((numbers[i], numbers[i + 1]))

# Print the final list of all consecutive pairs found
print("\nConsecutive Pairs List:")
print(consecutive_pairs)
