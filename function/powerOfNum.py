"""
Level 1
Write a function to calculate power of a number raised to other. E.g.- a^b.
"""

def power_num(n,p):
    ans = 1
    for i in range(1,p+1):
        ans = ans*n
    print(n,"^",p,"=",ans)

num = int(input("Enter Number:"))
power = int(input("Enter Power:"))
power_num(num,power)