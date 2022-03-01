"""
Level 2
Write a program to make a new string with the word "the" deleted in the sentence "This is the lion in the cage".
"""

str = "This is the lion in the cage"
str = str.split(" ")

lst = list(str)
list1 = []

for i in lst:
    if i=="the":
        del i
    else:
        list1.append(i)

str = ""

for i in list1:
    str = str+i+" "

print("String after deleting the:")
print(str)
