num = int(input("Enter a number: "))

# Initialize an empty list to store factors
factors = []
# Check for factors from 1 to num
for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)

# A prime number has exactly two distinct factors: 1 and itself
if len(factors) == 2:
    print(num, "is a Prime Number")
else:
# If the number is not prime, print its factors
    print("Factors:", end=" ")
    for factor in factors:
        print(factor, end=" ")
    print()
    print(num, "is not a Prime Number")