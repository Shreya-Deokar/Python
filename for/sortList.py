"""
Level 2
Sorting refers to arranging data in a particular format. Sort a list of integers in ascending order 
( without using built-in sorted function ). One of the algorithm is selection sort.
"""

list = [5,10,2,8,3,6]
print("Before Sorting:",list)

for i in range(1,len(list)):
    temp = list[i]
    j = i-1
    while(j>=0 and temp<=list[j]):
        list[j+1] = list[j]
        j = j-1
    list[j+1] = temp

print("After Sorting:",list)