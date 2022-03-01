"""
Level 1
Take 10 integer inputs from user and store them in a list and print them on screen.
"""

list = []
i=0
while i<10:
    n = int(input("Enter number:"))
    list.append(n)
    i = i+1

print(list)