""""
Create a class named 'Rectangle' with two data members- length and breadth and a method to claculate the area which is 'length*breadth'. The class 
has three constructors which are :
1 - having no parameter - values of both length and breadth are assigned zero.
2 - having two numbers as parameters - the two numbers are assigned as length and breadth respectively.
3 - having one number as parameter - both length and breadth are assigned that number.
Now, create objects of the 'Rectangle' class having none, one and two parameters and print their areas.
"""


class Rectangle:
    def __init__(self,*a):
        lst = list(a)

        if len(lst)==0:
            self.length = 0
            self.breadth = 0

        elif len(lst)==2:
            self.length = lst[0]
            self.breadth = lst[1]

        elif len(lst)==1:
            self.length = lst[0]
            self.breadth = lst[0]
    
    def area(self):
        a = self.length*self.breadth
        print("Area of Rectangle:",a)


rectArea = Rectangle()
rectArea.area()
rectArea1 = Rectangle(10,20)
rectArea1.area()
rectArea2 = Rectangle(5)
rectArea2.area()
