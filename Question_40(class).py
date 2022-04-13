"""write a program to print the duplicates number from the list . Print output in comma separated list
[12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23,01, 12,88,7,6,2].
"""
class Uniqu_e:
    def __init__(self,l):
        self.l=l

    def Unique(self,l):
        unique = []
        for i in l:
            if i not in unique:
                unique.append(i)
        print(unique)

l = [12, 24, 35, 70, 88, 120, 155, 99, 12, 7, 8, 93, 67, 47, 76, 34, 43, 76, 23, 1, 12, 88, 7, 6, 2]
obj=Uniqu_e(l)
obj.Unique(l)