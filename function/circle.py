"""
Level 1
Write a function to calculate area and circumference of a circle.
"""

def circle(r):
    area = 3.14*r*r
    print("Area of Circle:",area)
    circum = 2*3.14*r
    print("Circumference of Circle:",circum)

rad = float(input("Enter Radius of Circle:"))
circle(rad)