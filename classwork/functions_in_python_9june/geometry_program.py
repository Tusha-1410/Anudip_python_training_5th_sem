
# Program to use geometry module

# Importing the module
import geometry_module

# Rectangle
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

print("Rectangle Area =", geometry_module.area_rectangle(length, width))
print("Rectangle Perimeter =", geometry_module.perimeter_rectangle(length, width))

print()

# Square
side = float(input("Enter side of square: "))

print("Square Area =", geometry_module.area_square(side))
print("Square Perimeter =", geometry_module.perimeter_square(side))

print()

# Circle
radius = float(input("Enter radius of circle: "))

print("Circle Area =", geometry_module.area_circle(radius))
print("Circle Circumference =", geometry_module.perimeter_circle(radius))

