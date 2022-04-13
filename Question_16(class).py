'''Find the Smallest Number in a List
Create a function that takes a list of numbers and returns the smallest number in the list.'''
class small_list:
    def __init__(self,L):
        self.L=L
    def small(self,L):
        L.sort()
        print(L[0])
L=[]
n = int(input('Enter the  number of elements'))
for i in range(n):
    i=int(input("Enter the value "))
    L.append(i)
obj=small_list(L)
obj.small(L)

