'''Compare Strings by Count of Characters
Create a function that takes two strings as arguments and return either True or False depending on whether the
total number of characters in the first string is equal to the total number of characters in the second string.'''

def campare(str_1,str_2):
    if (len(str_1) == len(str_2)):
        return True
    else:
        return False

str_1=input('Enter the first string :  ')
str_2=input('Enter the second string : ')
print(campare(str_1,str_2))