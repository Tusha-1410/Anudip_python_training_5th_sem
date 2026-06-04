a = float(input("Enter first side: "))
if a <= 0:
    exit("invalid side")
b = float(input("Enter second side: "))
if b <= 0:
    exit("invalid side")
c = float(input("Enter third side: "))
if c <= 0:
    exit("invalid side")

if (a + b > c) and (a + c > b) and (b + c > a):
        print("The given sides form a triangle.")

        if a == b == c:
            print("It is an Equilateral Triangle.")
        elif a == b or b == c or a == c:
            print("It is an Isosceles Triangle.")
        else:
            print("It is a Scalene Triangle.")

else:
        print("The given sides do not form a triangle.")
 
