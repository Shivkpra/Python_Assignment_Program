# Return the First Element in a List

n=int(input('Enter the  number of elements'))
lis=[]
for i in range(n):                                        # loop used to append elements in list
    i=int(input("Enter the value "))
    lis.append(i)
print(lis)
for i in lis:
    print(i)
    break
