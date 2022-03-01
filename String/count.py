"""
Level 1
Write a program to find the number of vowels, consonents, digits and white space characters in a string.
"""

str = input("Enter string:")

vowel = 0
consonent = 0
digit = 0
space = 0

for i in range(0,len(str)):
    if str[i]=="a" or str[i]=="e" or str[i]=="i" or str[i]=="o" or str[i]=="u":
        vowel = vowel+1
    elif str[i]!="a" and str[i]!="e" and str[i]!="i" and str[i]!="o" and str[i]!="u" and str[i]>="a" and str[i]<="z":
        consonent = consonent+1
    elif str[i]>="0" and str[i]<="9":
        digit = digit+1
    elif str[i]==" ":
        space = space+1

print("Number of Vowels:",vowel)
print("Number of Consonents:",consonent)
print("Number Digits:",digit)
print("Number of Spaces:",space)