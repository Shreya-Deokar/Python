"""
Level 1
Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.
"""

list = []
reverse_list = []
i=0
while i<10:
    n = int(input("Enter number:"))
    list.append(n)
    i = i+1
print(list)

reverse_list = list.copy()

reverse_list.reverse()

print("Reverse List:",reverse_list)