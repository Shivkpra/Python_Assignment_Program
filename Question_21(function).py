'''
Check if an Integer is Divisible By Five
Create a function that returns True if an integer is evenly divisible by 5, and False otherwise.'''

def div( num):
    if (num % 5 == 0):
        return True
    else:
        return False


num = int(input('Enter the number'))
print(div(num))
