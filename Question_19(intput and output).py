'''Maximum Difference
Given a list of integers, return the difference between the largest and smallest integers in the list.'''
#Type 1 input and output
L=[]
n=int(input('Enter the  number of elements'))
for i in range(n):
    i=int(input("Enter the value "))
    L.append(i)
print(max(L)-min(L))
