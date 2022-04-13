'''Find the Smallest Number in a List
Create a function that takes a list of numbers and returns the smallest number in the list.'''
L=[]
n = int(input('Enter the  number of elements'))
for i in range(n):
    i=int(input("Enter the value "))
    L.append(i)
L.sort()
print(L)
print(L[0])