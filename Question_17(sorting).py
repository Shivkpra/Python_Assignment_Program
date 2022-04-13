'''Difference of Max and Min Numbers in List
Create a function that takes a list and returns the difference between the biggest and smallest numbers.
'''

L=[]
n = int(input('Enter the  number of elements'))
for i in range(n):
    i=int(input("Enter the value "))
    L.append(i)
L.sort()
print(L)
print(L[-1]-L[0])