"""Concant two list index wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
"""
def index_wise(list1,list2):                                               #function declaration
    list3 = [i + j for i, j in zip(list1, list2)]                          #adding element in list  from list1 and list2
    print(list3)

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
index_wise(list1,list2)                                                    #function call
