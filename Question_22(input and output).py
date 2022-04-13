'''Get the Sum of All List Elements
Create a function that takes a list and returns the sum of all numbers in the list.'''

L= []
n = int(input('How many numbers: '))
for i in range(n):
    i = int(input('Enter number '))
    L.append(i)
print("Sum of elements in given list is :", sum(L))
