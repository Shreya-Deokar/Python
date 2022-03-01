"""
Level 1
Print the following patterns using loop :
a.
*
**
***
****
b.
   *  
  *** 
 *****
  *** 
   *  
c.
1010101
 10101 
  101  
   1   
"""
"""
a.
*
**
***
****
"""

i=0
print("a.")
while i<=4:
    print("*"*i)
    i=i+1

"""
b.
   *  
  *** 
 *****
  *** 
   *  
"""

i=1
j=2
print("\nb.")
while i>=1:
   a = " "*j+"*"*i+" "*j
   print(a)
   i=i+2
   j=j-1
   if i>5:
      break
i=3
j=1
while i>=1:
   a = " "*j+"*"*i+" "*j
   print(a)
   i=i-2
   j=j+1


"""
c.
1010101
 10101 
  101  
   1 
"""

print("\nc.")
i = 7
s = 0
k=3
while (i>=0 and k>=0):
        a=(" "*s+"10"*k+"1"+" "*s)
        print(a)
        k=k-1
        i=i-2
        s=s+1