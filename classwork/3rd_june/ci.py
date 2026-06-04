p = float(input("Enter Principal Amount: "))
r = float(input("Enter Annual Interest Rate (%): "))
t = float(input("Enter Time (in years): "))

amount = p * (1 + r / 100) ** t
ci = amount - p

print("Compound Interest =", ci)
print("Total Amount =", amount)