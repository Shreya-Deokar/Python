"""
Level 2
A three digit number is called Armstrong number if sum of cube of its digit is equal to number itself.
E.g.- 153 is an Armstrong number because (1^3)+(5^3)+(3^3) = 153.
Write all Armstrong numbers between 100 to 500.
"""


print("Armstrong Numbers between 100 and 500:")

for i in range(100,501):
    sum = 0
    num = i
    while num>0:
        n1 = num%10
        sum = sum+n1**3
        num = num//10
        if sum==i:
            print(i)