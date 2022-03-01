"""
Level 1
Take 10 integer inputs from user and store them in a list. Again ask user to give a number. Now, 
tell user whether that number is present in list or not.
( Iterate over list using while loop ).
"""

list = []
i=0
while i<10:
    n = int(input("Enter number:"))
    list.append(n)
    i = i+1
print(list)

num = int(input("Enter a number to find in list:"))
i=0
while i<10:
    if num in list:
        print(num,"is present in list")
    else:
        print(num,"is not present in list")
    i = i+1