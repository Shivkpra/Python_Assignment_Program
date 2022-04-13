"""Concant two list index wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
"""
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]                             #adding element in list  from list1 and list2
print(list3)


