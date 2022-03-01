"""
Level 1
Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.
"""

num1 =int(input("Enter 1st Number:"))
num2 =int(input("Enter 2nd Number:"))

if num1>num2:
    smaller = num2
else:
    smaller = num1

for i in range(1,smaller):
    if ((num1%i==0) and (num2%i==0)):
        hcf = i

print("HCF of",num1,"and",num2,":",hcf)