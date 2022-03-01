"""
Level 2
Write a program to print a number given by user but digits reversed. E.g.-
INPUT : 123        OUTPUT : 321
INPUT : 12345        OUTPUT : 54321
"""

num = int(input("Enter Number:"))
rev_num = 0

while num>0:
    n1 = num%10
    rev_num = rev_num*10+n1
    num = num//10

print("Reverse is:",rev_num)