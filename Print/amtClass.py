"""
Suppose you have a Piggie Bank with an initial amount of $50 and you have to add some more amount to it. Create a class 'AddAmount' with a
data member named 'amount' with an initial value of $50. Now make two constructors of this class as follows:
1 - without any parameter - no amount will be added to the Piggie Bank
2 - having a parameter which is the amount that will be added to Piggie Bank
Create object of the 'AddAmount' class and display the final amount in Piggie Bank.
"""


class AddAmount:
    
    def __init__(self,*a):
        self.amount=50
        m=list(a)
        if len(m)>0:
            self.amount+=int(m[0])

    def totalamount(self):
        print("Total Amount:",self.amount)
    
amt2 = AddAmount(5000)
amt2.totalamount()

amt3 = AddAmount()
amt3.totalamount()