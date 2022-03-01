"""
Level 2
Calculate the sum of digits of a number given by user. E.g.-
INUPT : 123        OUPUT : 6
INUPT : 12345        OUPUT : 15
"""

num = int(input("Enter a Number:"))
num1 = num
sum = 0

while num>0:
    n1 = num%10
    sum = sum+n1
    num = num//10

print("Sum of digits of",num1,"is:",sum)