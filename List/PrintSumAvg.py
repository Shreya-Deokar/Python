"""
Level 1
Write a program to print sum, average of all numbers, smallest and largest element of a list.
"""

list = [5,10,15,20,25,30]
print(list)

sum = 0

for i in list:
    sum = sum+i

print("Sum of Elements in list:",sum)

avg = sum/len(list)
print("Average of elements in list:",avg)

print("Smallest Element:",min(list))
print("Largest Element:",max(list))