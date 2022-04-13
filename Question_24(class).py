'''Divides Evenly
Given two integers, a and b, return True if a can be divided evenly by b. Return False otherwise.'''

class divisible:
    def __init__(self,num_1,num_2):
        self.num_1=num_1
        self.num_2=num_2
    def div(self,num_1,num_2):
        if num_2 == 0:
            return "Invalid value of number 2"
        elif num_2 == 1:
            return True
        elif num_1 % num_2 == 0:
            return True
        else:
            return False
num_1=int(input('Enter the first number :  '))
num_2=int(input('Enter the second number : '))
obj=divisible(num_1,num_2)
print(obj.div(num_1,num_2))
