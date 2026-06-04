num = int(input("Enter a number: "))

# Check if the number is a palindrome
original = num
reverse = 0

# Calculate the reverse of the number
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse Number:", reverse)

# Check if the original number and the reverse are the same
if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")