"""Concant two list index wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
"""
class indexwis_e:                                                     #creating class
    def __init__(self,list1,list2):
        self.list1=list1
        self.list2=list2

    def index_wise(self,list1, list2):                                #function declaration
        list3 = [i + j for i, j in zip(list1, list2)]
        print(list3)

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
obj=indexwis_e(list1,list2)                                           # creating object to access class
obj.index_wise(list1, list2)
