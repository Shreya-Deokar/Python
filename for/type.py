"""
Level 1
From a list containing ints, strings and floats, make three lists to store them separately.
"""

list = [1,2,10.5,"python",5.5,"program",9,55.5]

ints = []
floats = []
strings = []

for i in list:
    if type(i)==int:
        ints.append(i)
    elif type(i)==float:
        floats.append(i)
    elif type(i)==str:
        strings.append(i)

print("List with int values:",ints)
print("List with float values:",floats)
print("List with string values:",strings)