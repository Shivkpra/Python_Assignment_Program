'''Find the Largest Number in a List
Create a function that takes a list of numbers. Return the largest number in the list.'''

class lar_list:
    def __init__(self,L):
        self.L=L
    def largest(self,L):
        L.sort()
        return (L[-1])
L=[]
n = int(input('Enter the  number of elements'))
for i in range(n):
    i=int(input("Enter the value "))
    L.append(i)
obj=lar_list(L)
print(obj.largest(L))
