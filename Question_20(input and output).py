'''
Return the Last Element in a List
Create a function that accepts a list and returns the last item in the list. The list can be either homogeneous or heterogeneous.'''
#type 1
lis=[]
n=int(input('Enter the  number of elements'))
for i in range(n):
    i=int(input("Enter the value "))
    lis.append(i)
print(lis)
print(lis[n-1])
print(lis[-1])
