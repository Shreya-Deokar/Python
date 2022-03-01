"""
Level 1
Sort the dictionary created in previous example according to marks.
"""

dict1 = {}

for i in range(1,11):
    name = input("Enter Name:")
    marks = int(input("Enter Marks:"))

    if name not in dict1:
        dict1[name]=marks
        
print(sorted(dict1.items(), key =lambda kv:(kv[1], kv[0]))) 