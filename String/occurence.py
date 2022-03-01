"""
Level 1
Write a program to find the first and the last occurence of the letter 'o' and character ',' in "Hello, World".
"""


str = "Hello, World"

print("First Occurence of letter o:",str.find("o"))
print("First Occurence of letter ,:",str.find(","))
print("Last Occurence of letter o:",str.rindex("o"))  #rindex is used to find last occurence
print("Last Occurence of letter ,:",str.rindex(","))