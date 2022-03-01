"""
Level 1
Create a Student class and initialize it with name and roll number. Make methods to :
1. Display - It should display all informations of the student.
2. setAge - It should assign age to student
3. setMarks - It should assign marks to the student.
"""



class Student:

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
    
    def setAge(self,age):
        self.age = age
    
    def setMarks(self,marks):
        self.marks = marks
    
    def display(self):
        print("Name:",self.name)
        print("Roll Number:",self.roll)
        print("Age:",self.age)
        print("Marks:",self.marks)

s = Student("Sonal",10)
s.setAge(20)
s.setMarks(100)
s.display()