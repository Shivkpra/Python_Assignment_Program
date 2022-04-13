# Return the First Element in a List

def list_first(lis):                                     # function declaration
    print(lis[0])                                        # print first value of list
n=int(input('Enter the  number of elements'))
lis=[]
for i in range(n):                                        # loop used to append elements in list
    i=int(input("Enter the value "))
    lis.append(i)
list_first(lis)
