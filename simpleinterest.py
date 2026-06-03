
principal = float(input("Enter principal: "))
if principal <= 0:
        print("Invalid Principal Amount!")
        exit()
rate = float(input("Enter rate (%): "))
if rate <= 0:
        print("Invalid Rate of Interest!")
        exit()
time = int(input("Enter time (years): "))
if time <= 0:
        print("Invalid Time!")
        exit()

simple_interest = (principal * rate * time) / 100
print("Simple Interest =", simple_interest)
