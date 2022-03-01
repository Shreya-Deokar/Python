"""
Level 1
You are given with a list of integer elements. Make a new list which will store square of elements of previous list.
"""

list = [1,2,3,4,5]

list1 = []
print(list)

for i in list:
    i = i**2
    list1.append(i)

print("New List with square of elements of previous list:")
print(list1)