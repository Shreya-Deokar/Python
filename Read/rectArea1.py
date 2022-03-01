"""
Ask user to give two float input for length and breadth of a rectangle and print area type casted to int.
"""

length = int(input("Enter Length of Rectangle:"))
breadth = int(input("Enter breadth of Rectangle:"))

area = length*breadth

print("Area of Rectangle:",int(area))