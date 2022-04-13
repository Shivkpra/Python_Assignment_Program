'''Divides Evenly
Given two integers, a and b, return True if a can be divided evenly by b. Return False otherwise.'''
#type 1 input and output
num_1=int(input('Enter the first number :  '))
num_2=int(input('Enter the second number : '))
if num_2==0:
    print("Invalid value of number 2")
elif num_2==1:
    print(True)
elif num_1%num_2==0:
    print(True)
else:
    print(False)