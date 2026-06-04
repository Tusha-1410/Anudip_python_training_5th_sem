correct_password = "admin123"

while True:
    password = input("Enter Password: ")

    if password.strip() == "":
        print("Password cannot be empty.")
        continue

    if password == correct_password:
        print("Login Successful.")
        break
    else:
        print("Invalid Password.")