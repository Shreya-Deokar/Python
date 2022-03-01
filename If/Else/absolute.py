"""
Level 1
Write a program to print absolute vlaue of a number entered by user. E.g.-
INPUT: 1        OUTPUT: 1
INPUT: -1        OUTPUT: 1
"""

num = int(input("Enter a Number:"))

#print("Absolute vale of",num,"is",abs(num))

if num<0:
    num=num*-1
    print("Absolute Value:",num)
else:
    print("Absolute Value:",num)