'''Concatenating Two Integer Lists
Create a function to concatenate two integer lists.'''

List_1=[]
List_2=[]
n = int(input('Enter the  number of elements  for list_1'))
for i in range(n):
    i=int(input("Enter the value "))

    List_1.append(i)
n1 = int(input("Enter the number of elements  for List_2"))
for j in range(n1):
    j=int(input("Enter the value "))
    List_2.append(j)
for i in List_2:
    List_1.append(i)
print(List_1)
