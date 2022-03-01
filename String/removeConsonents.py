"""
Level 1
Write a program to make a new string with all the consonents deleted from the string "Hello, have a good day".
"""

str = "Hello, have a good day"
lst = list(str)
list2 = []

for i in lst:
    if i!="a" and i!="e" and i!="i" and i!="o" and i!="u" and i!="A" and i!="E" and i!="I" and i!="O" and i!="U" and i!="," and i!=" ":
        del i
    else:
        list2.append(i)

str1 = " "
for i in list2:
    str1 = str1+i
print("String after removing consonents:",str1)
