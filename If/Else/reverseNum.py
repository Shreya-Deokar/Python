"""
Level 2
A 4 digit number is entered through keyboard. Write a program to print a new number with digits reversed as of orignal one. 
E.g.-
INPUT : 1234        OUTPUT : 4321
INPUT : 5982        OUTPUT : 2895
"""

num = int(input("Enter Number:"))
rev_num = 0

while num>0:
    n1 = num%10
    rev_num = rev_num*10+n1
    num = num//10

print("Reverse is:",rev_num)

