"""
Level 1
Write a function to calculate power of a number raised to other ( a^b ) using recursion.
"""

def power_num(n,p):
    if p==0:
        return 1
    elif p==1:
        return n
    else:
        return n*power_num(n,p-1)


num = int(input("Enter Number:"))
power = int(input("Enter Power:"))
print(num,"^",power,"=",power_num(num,power))