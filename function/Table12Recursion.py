"""
Level 1
Print multiplication table of 12 using recursion.
"""

def table12(n,i):
    if i>10:
        return 
    print(n,"*",i,"=",n*i)
    return table12(n,i+1)


table12(12,1)