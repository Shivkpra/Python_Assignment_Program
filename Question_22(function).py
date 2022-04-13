'''Get the Sum of All List Elements
Create a function that takes a list and returns the sum of all numbers in the list.'''


def add(L):
    sum=0
    for i in L:
        sum=sum+i
    return sum

L = []
sum = 0
n = int(input('Enter the number of element'))
for i in range(n):
    i = int(input('Enter the value'))
    L.append(i)
print(add(L))