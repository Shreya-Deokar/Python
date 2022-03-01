"""
Level 1
From the two list obtained in previous question, make new lists, containing only numbers which 
are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.
"""
list_even = []
list_odd = []

for i in range(1,101):
    if i%2==0:
        list_even.append(i)
    elif i%2!=0:
        list_odd.append(i)

div_4 = []
div_6 = []
div_8 = []
div_10 = []
div_3 = []
div_5 = []
div_7 = []
div_9 = []

for i in list_even:
    if i%4==0:
        div_4.append(i)
    if i%6==0:
        div_6.append(i)
    if i%8==0:
        div_8.append(i)
    if i%10==0:
        div_10.append(i)
    if i%3==0:
        div_3.append(i)
    if i%5==0:
        div_5.append(i)
    if i%7==0:
        div_7.append(i)
    if i%9==0:
        div_9.append(i)

for i in list_odd:
    if i%3==0:
        div_3.append(i)
    if i%5==0:
        div_5.append(i)
    if i%7==0:
        div_7.append(i)
    if i%9==0:
        div_9.append(i)


print("Divisible of 4:",div_4)
print("Divisible of 6:",div_6)
print("Divisible of 8:",div_8)
print("Divisible of 10:",div_10)
print("Divisible of 3:",div_3)
print("Divisible of 5:",div_5)
print("Divisible of 7:",div_7)
print("Divisible of 9:",div_9)