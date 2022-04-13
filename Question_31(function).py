"""Write a program to square each odd number in a list.
Take a list - list contains at least 20 elements
"""
def odd_square(list):
    odd_sq = []
    odd = []
    for i in list:
        if i % 2 != 0:
            odd.append(i)
            i = i * i
            odd_sq.append(i)

    print(odd)
    print (odd_sq)


list=[]

n=int(input("Enter the number of element in list( min  20 value) "))
for i in range (n):
    i=int(input(F"Enter the value {i} :" ))
    list.append(i)
odd_square(list)

