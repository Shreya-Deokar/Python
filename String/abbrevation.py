"""
Level 1
Write a program that takes your full name as input and displays the abbreviations of the first and middle 
names except the last name which is displayed as it is. 
For example, if your name is Robert Brett Roser, then the output should be R.B.Roser.
"""

name = "Robert Brett Roser"
print("Name:",name)

name_split = name.split(" ")

abbreviation = name_split[0][0]+ "." + name_split[1][0]+ "." + name_split[2]
#[0][0] = first split's first letter
# [1][0] = second slpit's first letter
# [2] =  third split

print("Abbrevation:",abbreviation)