"""
Level 1
Ask user to give integer inputs to make a list. Store only even values given and print the list.
"""

num = int(input("Enter how many integers:"))

i = 0
list = []

for i in range(1,num+1):
    list_num = int(input("Enter list elements:"))
    if list_num%2==0:
        list.append(list_num)

print("List with even values:",list)