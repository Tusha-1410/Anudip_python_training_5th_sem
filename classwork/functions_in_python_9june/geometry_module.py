# geometry.py
# Module for Area and Perimeter of 2D Figures

# Function to calculate area of a rectangle
def area_rectangle(length, width):
    return length * width


# Function to calculate perimeter of a rectangle
def perimeter_rectangle(length, width):
    return 2 * (length + width)


# Function to calculate area of a square
def area_square(side):
    return side * side


# Function to calculate perimeter of a square
def perimeter_square(side):
    return 4 * side


# Function to calculate area of a circle
def area_circle(radius):
    pi = 3.14
    return pi * radius * radius


# Function to calculate circumference (perimeter) of a circle
def perimeter_circle(radius):
    pi = 3.14
    return 2 * pi * radius
