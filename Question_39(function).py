"""write a program to print the list after removing the 0th,4th,5th numbers from list
List [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23,01].
"""
def remove(List,n):
    List.pop(n)
    print(List)
List = [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23,1]
n=int(input("Enter the index you want to remove"))
remove(List,n)
List = [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23,1]
n=int(input("Enter the index you want to remove"))

remove(List,n)
List = [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23,1]
n=int(input("Enter the index you want to remove"))

remove(List,n)
