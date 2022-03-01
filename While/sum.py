"""
Level 1
Take 10 integers from keyboard using loop and print their average value on the screen.
"""
sum = 0
i=0
while i<10:
    num = int(input("Enter number:"))
    sum = sum+num
    i = i+1

print("Average of Numbers:",sum/10.0)