"""
Level 1
Create a Cricle class and intialize it with radius. Make two methods getArea and getCircumference inside this class.
"""

class Circle:

    def __init__(self,r):
        self.r = r
    
    def getArea(self):
        area = 3.14*self.r*self.r
        print("Area of Circle:",area)
    
    def getCircumference(self):
        circumference = 2*3.14*self.r
        print("Circumference of Circle:",circumference)


c = Circle(5)
c.getArea()
c.getCircumference()
