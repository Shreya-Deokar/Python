"""
Level 2
Write down the names of 10 of your friends in a list and then sort those in alphabetically ascending order.
"""
name = []

for i in range(1,11):
    names = input("Enter Names of your friends:")
    name.append(names)

name.sort()

str = ""

for i in name:
    str = str+i+", "

print("Name is Sorted Ascending Order:")
print(str)