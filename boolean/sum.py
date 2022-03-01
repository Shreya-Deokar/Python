"""
Take two number and check whether the sum is greater than 5, less than 5 or equal to 5.
"""

num1 = int(input("Enter 1st Number:"))
num2 = int(input("Enter 2nd Number:"))

sum = num1+num2

if sum>5:
    print("Sum is Greater than 5")
elif sum<5:
    print("Sum is Less than 5")
elif sum==5:
    print("Sum is Equal to 5")