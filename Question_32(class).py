"""Write a program that computes the net amount of a bank account based on a transaction log from console input.
Log format is :  D 100 W 200
D means deposit while W means withdrawal. Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 Then, the output should be: 500
"""
class Account:
    def __init__(self,D,W):
        self.D=D
        self.W=W

    def Net_amount(self,D, W):
        print(F"Log Foramt is D {D} and W {W}")
        net_amount = D - W
        print("Net amount in your account is:", net_amount)

D=float(input("Enter the deposit amount"))
W=float(input("Enter the withdrawal amount"))
obj=Account(D,W)
obj.Net_amount(D,W)
