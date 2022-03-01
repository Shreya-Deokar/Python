"""
Level 1
Take a list of 10 elements. Split it into middle and store the elements in two dfferent lists. E.g.-
INITIAL list :
58	24	13	15	63	9	8	81	1	78

After spliting :
58	24	13	15	63
9	8	81	1	78
"""

list = [58,24,13,15,63,9,8,81,1,78]

length = len(list)//2

l1 = list[:length]
l2 = list[length:]

print("1st Split of List:",l1)
print("2nd Split of List:",l2)