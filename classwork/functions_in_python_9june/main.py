# create a program which provides a menu 
#  to the user to select the two dimensional figure
#  (circle,rectangle,square).After selecting the figure 
# the user is again asked to provide the input of corresponding data
#  for the figure , after input of data again provide a menu to select
#  the operation that is area, perimeter and as per the data provided 
# or operation selected by the user..display the result of operation.
#  This task will be repeated again and again until user selects the
#  option to exit from that figure.
#-------------------------------------------------------------------

# main.py
# Menu Driven Program using geometry module

import geometry

while True:

    print("\n========== 2D FIGURE MENU ==========")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # ---------------- CIRCLE ----------------
    if choice == 1:

        radius = float(input("Enter Radius: "))

        while True:
            print("\n--- Circle Operations ---")
            print("1. Area")
            print("2. Perimeter")
            print("3. Exit Circle")

            op = int(input("Enter Operation: "))

            if op == 1:
                area = geometry.area_circle(radius)
                print("Area of Circle =", area)

            elif op == 2:
                perimeter = geometry.perimeter_circle(radius)
                print("Perimeter of Circle =", perimeter)

            elif op == 3:
                print("Exiting Circle Menu...")
                break

            else:
                print("Invalid Choice!")

    # ---------------- RECTANGLE ----------------
    elif choice == 2:

        length = float(input("Enter Length: "))
        width = float(input("Enter Width: "))

        while True:
            print("\n--- Rectangle Operations ---")
            print("1. Area")
            print("2. Perimeter")
            print("3. Exit Rectangle")

            op = int(input("Enter Operation: "))

            if op == 1:
                area = geometry.area_rectangle(length, width)
                print("Area of Rectangle =", area)

            elif op == 2:
                perimeter = geometry.perimeter_rectangle(length, width)
                print("Perimeter of Rectangle =", perimeter)

            elif op == 3:
                print("Exiting Rectangle Menu...")
                break

            else:
                print("Invalid Choice!")

    # ---------------- SQUARE ----------------
    elif choice == 3:

        side = float(input("Enter Side: "))

        while True:
            print("\n--- Square Operations ---")
            print("1. Area")
            print("2. Perimeter")
            print("3. Exit Square")

            op = int(input("Enter Operation: "))

            if op == 1:
                area = geometry.area_square(side)
                print("Area of Square =", area)

            elif op == 2:
                perimeter = geometry.perimeter_square(side)
                print("Perimeter of Square =", perimeter)

            elif op == 3:
                print("Exiting Square Menu...")
                break

            else:
                print("Invalid Choice!")

    # ---------------- EXIT ----------------
    elif choice == 4:
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please Try Again.")
        