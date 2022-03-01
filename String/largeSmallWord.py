"""
Level 2
Write a program to find out the largest and smallest word in the string "This is an umbrella".
"""
str = "This is an umbrella"

str = str.split(" ")

large = len(str[0])

for i in str:
    if len(i)>large:
        large = len(i)
        max = i
print("Largest:",max)

small = len(str[0])

for i in str:
    if len(i)<small:
        small = len(i)
        min = i
print("Smallest:",min)

