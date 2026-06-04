num = int(input("Enter a positive number: "))

#store the original number in a temporary variable
temp = num
digits = len(str(num))
sum_of_powers = 0

#calculate the sum of the digits raised to the power of the number of digits
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** digits
    temp = temp // 10

#check if the calculated sum is equal to the original number
if sum_of_powers == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")
