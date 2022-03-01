"""
Level 1
Print multiplication table of 14 from a list in which multiplication table of 12 is stored.
"""

table12 = []

for i in range(1,121):
    if i%12==0:
        table12.append(i)

print(table12)

print(list(enumerate(table12)))

table14=[] 
for i, j in enumerate(table12):
    table14.append(j+(i+1)*2)

print(table14)