"""
Level 1
Ask user to give name and marks of 10 different students. Store them in dictionary.
"""

dict1 = {}

for i in range(1,11):
    name = input("Enter Name:")
    marks = int(input("Enter Marks:"))

    if name not in dict1:
        dict1[name]=marks

print(dict1)