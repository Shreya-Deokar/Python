"""
A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.
"""

held = int(input("Enter Number of Classes Held:"))
attend = int(input("Enter Number of Classes Attended:"))

per = (attend/held)*100

print("Percentage of Class Attended:",per)

if per>=75:
    print("Student Will Allowed to Sit in Exam")
else:
    print("Student Will Not Allowed to Sit in Exam")
