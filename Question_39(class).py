"""write a program to print the list after removing the 0th,4th,5th numbers from list
List [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23,01].
"""
class remov_e:
    def __init__(self,List,n):
        self.List=List
        self.n=n

    def remove(self,List, n):
        List.pop(n)
        print(List)

List = [12, 24, 35, 70, 88, 120, 155, 99, 12, 7, 8, 93, 67, 47, 76, 34, 43, 76, 23, 1]
n = int(input("Enter the index you want to remove"))
obj=remov_e(List,n)
obj.remove(List, n)
List = [12, 24, 35, 70, 88, 120, 155, 99, 12, 7, 8, 93, 67, 47, 76, 34, 43, 76, 23, 1]
n = int(input("Enter the index you want to remove"))
obj1=remov_e(List,n)
obj1.remove(List, n)
List = [12, 24, 35, 70, 88, 120, 155, 99, 12, 7, 8, 93, 67, 47, 76, 34, 43, 76, 23, 1]
n = int(input("Enter the index you want to remove"))
obj2=remov_e(List,n)
obj2.remove(List, n)
