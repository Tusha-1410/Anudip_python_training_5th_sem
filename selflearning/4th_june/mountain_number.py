# Read a number from the user
num = int(input("Enter a positive number: "))

# Convert the number to a string so we can examine its digits one by one
num_str = str(num)

# A mountain number must have at least three digits to go up then down
if len(num_str) < 3:
	print("Not a Mountain Number")
else:
	# Find the peak position: digits must strictly increase until the peak
	i = 0
	while i + 1 < len(num_str) and int(num_str[i + 1]) > int(num_str[i]):
		i += 1

	# The peak cannot be the first or last digit
	if i == 0 or i == len(num_str) - 1:
		print("Not a Mountain Number")
	else:
		# After the peak, digits must strictly decrease
		is_mountain = True
		while i + 1 < len(num_str):
			if int(num_str[i + 1]) >= int(num_str[i]):
				is_mountain = False
				break
			i += 1

		if is_mountain:
			print("Mountain Number")
		else:
			print("Not a Mountain Number")
