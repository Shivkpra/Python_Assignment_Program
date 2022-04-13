'''Compare Strings by Count of Characters
Create a function that takes two strings as arguments and return either True or False depending on whether the
total number of characters in the first string is equal to the total number of characters in the second string.'''
#type 1 input and output
str_1=input('Enter the first string :  ')
str_2=input('Enter the second string : ')
cout_1=0
cout_2=0
for i in str_1:
    cout_1+=1
for i in str_2:
    cout_2+=1
if (cout_1==cout_2):
    print(True)
else:
    print(False)