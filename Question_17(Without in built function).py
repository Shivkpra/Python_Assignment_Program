'''Difference of Max and Min Numbers in List
Create a function that takes a list and returns the difference between the biggest and smallest numbers.
'''

def min_lis(L,ele):
    for i in range(len(L)):
        for j in range(i + 1, len(L)):

            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]
    return L[0]

def max_list(L,ele):
    for i in range(len(L)):
        for j in range(i + 1, len(L)):

            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]

    return (L[-1])
L=[]
ele=0
n = int(input('Enter the  number of elements'))
for i in range(n):
    i=int(input("Enter the value "))
    L.append(i)
    ele+=1
print(max_list(L,ele)-min_lis(L,ele))