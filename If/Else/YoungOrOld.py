"""
Level 1
Take input of age of 3 people by user and determine oldest and youngest among them.
"""
a1 = int(input("Enter age of 1st person:"))
a2 = int(input("Enter age of 2nd person:"))
a3 = int(input("Enter age of 3rd person:"))

if a1>a2 and a1>a3:
    print("Person with Age",a1,"is Oldest")
elif a2>a3 and a2>a1:
    print("Person with Age",a2,"is Oldest")
elif a3>a1 and a3>a2:
    print("Person with Age",a3,"is Oldest")

if a1<a2 and a1<a3:
    print("Person with Age",a1,"is Youngest")
elif a2<a3 and a2<a1:
    print("Person with Age",a2,"is Youngest")
elif a3<a1 and a3<a2:
    print("Person with Age",a3,"is Youngest")
