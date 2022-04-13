'''Get the Sum of All List Elements
Create a function that takes a list and returns the sum of all numbers in the list.'''

class sum_list:
    def __init__(self,L):
        self.L=L

    def add(self,L):
        sum = 0
        for i in L:
            sum = sum + i
        return sum
L = []
n = int(input('Enter the number of element'))
for i in range(n):
    i = int(input('Enter the value'))
    L.append(i)
obj=sum_list(L)
print(obj.add(L))
