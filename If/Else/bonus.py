"""
Level 1
A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.
"""

sal = float(input("Enter Salary:"))
service = int(input("Enter Year of Service:"))

if service>5:
    sal = sal+sal*0.5
    print("Net Bonus:",sal)
elif service<5:
    print("No Bonus")