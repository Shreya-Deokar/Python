"""
Level 1
Initialize and print each element in new line of a list inside list.
"""

list = [[1,2,3,4],[5,6,7,8]]

for i in list:
    for j in i:
        print(j, end = ' ')
    print('', sep='\n')
