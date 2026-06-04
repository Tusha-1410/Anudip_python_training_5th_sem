rows = int(input("Enter number of rows (positive number): "))

# Generate the number pyramid
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
