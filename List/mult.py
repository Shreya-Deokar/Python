"""
Level 1
Write a program to find the product of all elements of a list.
"""

list = [10,20,30,40,50]
print(list)

mult = 1

for i in list:
    mult = mult*i

print("Multiplication of elements of list:",mult)