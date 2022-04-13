'''Find the Largest Number in a List
Create a function that takes a list of numbers. Return the largest number in the list.'''

def max_lis(L,ele):
    for i in range(len(L)):
        for j in range(i + 1, len(L)):

            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]

    print(L)
    print(L[-1])
L=[]
ele=0
n = int(input('Enter the  number of elements'))
for i in range(n):
    i=int(input("Enter the value "))
    L.append(i)
    ele+=1
max_lis(L,ele)
