'''Difference of Max and Min Numbers in List
Create a function that takes a list and returns the difference between the biggest and smallest numbers.
'''

class difference:
    def __init__(self,L):
        self.L=L
    def differ(self,L):
        L.sort()
        print((L[-1]-L[0]))

L=[]
n = int(input('Enter the  number of elements'))
for i in range(n):
    i=int(input("Enter the value "))
    L.append(i)

obj=difference(L)
obj.differ(L)