"""
Level 1
Write a function to find factorial of a number but also store the factorials 
calculated in a dictionary as done in the Fibonacci series example.
"""

def fact(n):
    dict1 = {}
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    print("Factorial of",n,"is:",fact)
    dict1[n]=fact
    print(dict1)

num = int(input("Enter a Number:"))
fact(num)