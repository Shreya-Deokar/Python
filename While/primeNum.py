"""
Level 2
Write a program to print all prime number in between 1 to 100.
"""

print ("The Prime Numbers between 1 to 100: ")  
for num in range (1,101):  
    if num > 1:  
        for i in range (2, num):  
            if (num % i) == 0:  
                break  
        else:  
            print (num)