"""
Level 1
Make a list by taking 10 input from user. Now delete all repeated elements of the list.
E.g.-
INPUT : [1,2,3,2,1,3,12,12,32]
OUTPUT : [1,2,3,12,32]
"""

list = [1,2,3,2,1,3,12,12,32] 
print(list)
list1 = []

for i in list:
    if i in list1:
        del i
    elif i not in list1:
        list1.append(i)

print("List after deleting repeated elements:",list1)