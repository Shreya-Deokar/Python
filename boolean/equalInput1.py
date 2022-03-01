"""
Take 3 inputs from user and check :
all are equal
any of two are equal
( use and or )
"""

input1 = input("Enter 1st input:")
input2 = input("Enter 2nd input:")
input3 = input("Enter 3rd input:")

print("3 Inputs are Same(AND):",input1==input2 and input2==input3 and input3==input1)
print("3 Inputs are Same(OR):",input1==input2 or input2==input3 or input3==input1)