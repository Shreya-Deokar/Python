"""
Level 1
Take inputs from user to make a list. Again take one input from user and search it in the 
list and delete that element, if found. Iterate over list using for loop.
"""
num = int(input("Enter how many elements:"))

lst = []
for i in range(1,num+1):
    ele = int(input("Enter element:"))
    lst.append(ele)

n = int(input("Enter number to search in list:"))

lst1 = []
for i in lst:
    if i==n:
        del i
    else:
        lst1.append(i)

print(lst1)