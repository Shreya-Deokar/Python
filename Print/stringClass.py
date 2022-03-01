"""
Create a class named 'Programming'. While creating an object of the class, if nothing is passed to it, then the
message "I love programming languages" should be printed. If some String is passed to it, then in place of "programming languages" the name 
of that String variable should be printed.
For example, while creating object if we pass "Python", then "I love Python" should be printed.
"""

class Programming:

    def __init__(self,*st):
        if len(st)==0:
            print("I love programming languages")
        else:
            st1 = ""
            for i in st:
                st1 = st1+i
            print("I love",st1)

st1 = Programming()
st2 = Programming("Python")