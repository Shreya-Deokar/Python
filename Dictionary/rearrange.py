"""
Level 1
Take a list containg only strings. Now, take a string input from user and rearrange the elements of the list 
according to the number of occurence of the string taken from user in the elements of the list.
E.g.-LIST : ["no bun","bug bun bug bun bug bug","bunny bug","buggy bug bug buggy"]
STRING TAKEN : "bug"
OUTPUT LIST:["bug bun bug bun bug bug","buggy bug bug buggy","bunny bug","no bun"]
"""

a = ["no bun","bug bun bug bun bug bug","bunny bug","buggy bug bug buggy"]

print(a)

b = input(("Enter any word to rearrange:"))

c = {}

for i in a:

  count = 0

  for j in i.split():

    if j == b:

      count = count+1

  c[count]=i

d = []

for s in sorted(c):

  d.append(c[s])

d.reverse()

print (d)