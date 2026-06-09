# geometry.py
# Functions for Area and Perimeter of 2D Figures

# Rectangle Functions
def area_rectangle(length, width):
    return length * width

def perimeter_rectangle(length, width):
    return 2 * (length + width)


# Square Functions
def area_square(side):
    return side * side

def perimeter_square(side):
    return 4 * side


# Circle Functions
def area_circle(radius):
    return 3.14 * radius * radius

def perimeter_circle(radius):
    return 2 * 3.14 * radius
