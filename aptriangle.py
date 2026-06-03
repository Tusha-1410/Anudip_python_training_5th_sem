

# Input sides of the triangle
a = float(input("Enter side a(in cm): "))
b = float(input("Enter side b(in cm): "))
c = float(input("Enter side c(in cm): "))
print("------------------------")
print("side a is" ,a ,"cm")
print("side b is" ,b ,"cm")
print("side c is" ,c ,"cm")


# Perimeter
perimeter = a + b + c

s = perimeter/2

# Area using Heron's formula
area = (s * (s - a) * (s - b) * (s - c))**0.5

print("Perimeter =", perimeter ,"cm")
print("Area =", area ,"sq.cm")