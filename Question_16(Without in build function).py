'''Find the Smallest Number in a List
Create a function that takes a list of numbers and returns the smallest number in the list.'''
def min_lis(L,ele):
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]

    print(L)
    print("Smallest number",L[0])

L=[]
ele=0
n = int(input('Enter the  number of elements'))
for i in range(n):
    i=int(input("Enter the value "))
    L.append(i)
    ele+=1
min_lis(L,ele)     # function call