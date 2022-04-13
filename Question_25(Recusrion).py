'''

Create a recursive function that takes two parameters and repeats the string n number of times. The first parameter text
 is the string to be repeated and the second parameter is the number of times the string is to be repeated.'''
# Recusrion
def string(str,n):
    while n>0:
        print(str)
        return string(str,n-1)


str=input('Enter the string:')
n=int(input('How many time you want to print the string: '))
string(str,n)
