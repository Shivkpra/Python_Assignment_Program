def min_lis(L,ele):

    for i in range(ele):
        for j in range(i + 1, ele):

            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]


    return (L[0])
def max_list(L,ele):
    for i in range(ele):
        for j in range(i + 1, ele):

            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]

    return L[-1]
L=[]
ele=0
n = int(input('Enter the  number of elements'))
for i in range(n):
    i=int(input("Enter the value "))
    L.append(i)
    ele+=1
print(max_list(L,ele)-min_lis(L,ele))