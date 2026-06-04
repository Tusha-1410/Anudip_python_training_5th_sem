import math

# Input sides of the triangle
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# Perimeter
perimeter = a + b + c

s = perimeter/2

# Area using Heron's formula
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("Perimeter =", perimeter)
print("Area =", area)