"""Write a program that computes the net amount of a bank account based on a transaction log from console input.
Log format is :  D 100 W 200
D means deposit while W means withdrawal. Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 Then, the output should be: 500
"""
D=float(input("Enter the deposit amount"))
W=float(input("Enter the withdrawal amount"))
print(F"Log Foramt is D {D} and W {W}")
net_amount=D-W
print("Net amount in your account is:",net_amount)
