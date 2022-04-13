'''
Check if an Integer is Divisible By Five
Create a function that returns True if an integer is evenly divisible by 5, and False otherwise.'''

class div:
    def __init__(self,num):
        self.num=num

    def div( self,num):
        if (num % 5 == 0):
            return True
        else:
            return False

num = int(input('Enter the number'))
obj=div(num)
print(obj.div(num))
