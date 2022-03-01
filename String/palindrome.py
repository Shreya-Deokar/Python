"""
Level 2
Write a program to check if a given string is a Palindrome.
A palindrome reads same from front and back e.g.- aba, ccaacc, mom, etc.
"""

str = input("Enter String:")
str1 = ""

for i in str:
    str1 = i+str1

if str1==str:
    print(str,"is Palindrome")
else:
    print(str,"is not a Palindrome")