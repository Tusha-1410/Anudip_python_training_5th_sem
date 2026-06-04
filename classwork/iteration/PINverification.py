correct_pin = 1234

while True:
    pin = input("Enter PIN: ")

    if not pin.isdigit():
        print("Invalid Input! Please enter numbers only.")
        continue

    if int(pin) == correct_pin:
        print("Access Granted.")
        break
    else:
        print("Incorrect PIN. Try Again.")