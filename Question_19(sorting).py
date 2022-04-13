L=[]
n = int(input('Enter the  number of elements'))
for i in range(n):
    i=int(input("Enter the value "))
    L.append(i)
L.sort()
print(L)
print(L[-1]-L[0])

