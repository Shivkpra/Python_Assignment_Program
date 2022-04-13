"""Write a program to square each odd number in a list.
Take a list - list contains at least 20 elements
"""
list=[10,34 ,56,78 ,90,45,54,12,15,17,18,19,20,35,59,51,67,66,33 ,85,96]
odd_sq=[]
odd=[]
for i in list:
    if i%2!=0:
        odd.append(i)

        i=i*i
        odd_sq.append(i)
print(odd)
print(odd_sq)
