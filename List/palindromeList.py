"""
Level 1
Write a program to check if elements of a list are same or not it read from front or back. 
E.g.- 2	3	15 	15	3	2
"""

list = [2,3,15,15,3,2]

mid= (len(list))/2
same = True
i=0
while i<mid:
    if list[i]!=list[len(list)-i-1]:
        print("Not a Same")
        same = False
        break
    i = i+1
if same == True:
    print("Same")