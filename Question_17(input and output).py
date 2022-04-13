'''Difference of Max and Min Numbers in List
Create a function that takes a list and returns the difference between the biggest and smallest numbers.
'''
#Type 1 input and output
L=[]
n=int(input('Enter the  number of elements'))
for i in range(n):
    i=int(input("Enter the value "))
    L.append(i)
print(max(L)-min(L))
