a1 = float(input("enter first angle : "))
if(a1 <= 0):
    exit("angle must be positive")
a2 = float(input("enter second angle : "))
if(a2 <= 0):
    exit("angle must be positive")
a3 = float(input("enter third angle : "))
if(a3 <= 0):
    exit("angle must be positive")

if(a1 + a2 + a3 == 180):
    print("above angles form a triangle")
else:
    print("triangle formation not possible")