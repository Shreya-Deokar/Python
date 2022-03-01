"""
Level 1
Take 20 integer inputs from user and print the following:
number of positive numbers
number of negative numbers
number of odd numbers
number of even numbers
number of 0s.
"""

list = []
i=0
while i<20:
    n = int(input("Enter number:"))
    list.append(n)
    i = i+1
print(list)

cnt_p = 0   #positive count
cnt_n = 0   #negative count
cnt_o = 0   #odd count
cnt_e = 0   #even count
cnt_z = 0   #zero count

for i in list:
    if i>0:
        cnt_p = cnt_p+1
print("Number of Positive integers in list:",cnt_p)

for i in list:
    if i<0:
        cnt_n = cnt_n+1
print("Number of Negative integers in list:",cnt_n)

for i in list:
    if i%2!=0:
        cnt_o = cnt_o+1
print("Number of Odd integers in list:",cnt_o)

for i in list:
    if i%2==0:
        cnt_e = cnt_e+1
print("Number of Even integers in list:",cnt_e)

for i in list:
    if i==0:
        cnt_z = cnt_z+1
print("Number of Zeros in list:",cnt_z)