# Initialize an empty list to store the numbers
numbers = []

# Input 20 numbers from the user
for i in range(20):
    # Append each number entered by the user to the list
    numbers.append(int(input(f"Enter  a positive number {i+1}: ")))

print("Original List:", numbers)
# Ask the user for the target number to remove duplicates of
target = int(input("Enter any positive number: "))

# Count the frequency of the target number in the list
frequency = numbers.count(target)
if frequency == 0:
    print(f"The number {target} is not in the list.")
elif frequency == 1:
    print(f"The number {target} appears only once in the list.")
else:
    numbers.reverse()  
# Reverse the list to remove duplicates from the end
    for i in range(1, frequency):
        numbers.remove(target)  # Remove the target number until only one instance remains
    numbers.reverse()  # Reverse the list back to its original order
    print("Updated List:", numbers)
