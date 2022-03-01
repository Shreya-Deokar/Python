"""
Leve1 1
Using range(1,101), make two list, one containing all even numbers and other containing all odd numbers.
"""

list_even = []
list_odd = []

for i in range(1,101):
    if i%2==0:
        list_even.append(i)
    elif i%2!=0:
        list_odd.append(i)

print("List with even numbers:")
print(list_even)
print("List with odd numbers:")
print(list_odd)