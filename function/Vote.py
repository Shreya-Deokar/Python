"""
Level 1
Write a function to tell user if he/she is able to vote or not.
( Consider minimum age of voting to be 18. )
"""

def vote(a):
    if a>=18:
        print("User Able to Vote")
    else:
        print("User Not Able to Vote")

age = int(input("Enter Age:"))
vote(age)