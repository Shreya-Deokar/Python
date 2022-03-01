"""
Level 1
A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.
"""


qty = int(input("Enter Quantity:"))
cost = qty*100

if cost>1000:
    cost = cost-cost*0.1
    print("Cost after discount:",cost)
else:
    print("No discount")