"""
Level 1
Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical 
cause or not ( 'Y' or 'N' ) and print accordingly.
"""

held = int(input("Enter Number of Classes Held:"))
attend = int(input("Enter Number of Classes Attended:"))

per = (attend/held)*100

print("Percentage of Class Attended:",per)

if per>=75:
    print("Student Will Allowed to Sit in Exam")
elif per<75:
    medical = input("Having Medical Cause(Y/N):")
    if medical=="Y":
        print("Student Will Allowed to Sit in Exam")
    elif medical=="N":
        print("Student Will Not Allowed to Sit in Exam")
   