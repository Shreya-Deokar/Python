"""
Level 2
Using range(1,101), make a list containing only prime numbers.
"""

for num in range(1,101):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)