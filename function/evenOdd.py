"""
Level 1
Write a function to check if a number is even or not.
"""
def even_odd(n):
    if n%2==0:
        print(n,"is Even")
    else:
        print(n,"is Odd")


num = int(input("Enter a Number:"))
even_odd(num)