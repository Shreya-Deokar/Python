"""
Level 1
Write a function to calculate area and perimeter of a rectangle.
"""

def rectangle(l,b):
    area = l*b
    print("Area of Rectangle:",area)
    perimeter = 2*(l+b)
    print("Perimeter of Rectangle:",perimeter)

length = float(input("Enter Length of Rectangle:"))
breadth = float(input("Enter Breadth of Rectangle:"))
rectangle(length,breadth)