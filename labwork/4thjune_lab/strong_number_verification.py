num = int(input("Enter a positive number: "))

#store the original number in a temporary variable
temp = num
sum_fact = 0

#calculate the sum of the factorial of each digit
while temp > 0:
    digit = temp % 10

    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i

    sum_fact = sum_fact + fact
    temp = temp // 10

#check if the calculated sum is equal to the original number
if sum_fact == num:
    print(num, "is a Strong Number")
else:
    print(num, "is not a Strong Number")
