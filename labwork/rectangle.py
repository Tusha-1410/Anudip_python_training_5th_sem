length = float(input("Enter length of rectangle: "))
if length <= 0:
        print("invalid length")
        exit()
breadth = float(input("Enter breadth of rectangle: "))
if breadth <=0:
        print("invalid breadth")
        exit()


area = length * breadth
perimeter = 2 * (length + breadth)

print("\nRectangle Details")
print("-----------------")
print("Length =", length)
print("Breadth =", breadth)
print("Area =", area, "sq. units")
print("Perimeter =", perimeter, "units")

