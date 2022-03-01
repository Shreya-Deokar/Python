"""
Level 1
Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that 
determines and prints all the perfect numbers between 1 and 1000.
[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), 
sum to the number. E.g., 6 is a perfect number because 6=1+2+3].
"""

def perfect():
    for i in range(1,1001):
        sum1 = 0
        for j in range(1,i-1):
            if(i%j==0):
                sum1 = sum1+j
        if sum1==i:
            print(i)

print("Perfect Numbers Between 1 to 1000:")
perfect()