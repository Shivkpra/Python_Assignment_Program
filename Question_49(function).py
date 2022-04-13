"""Concatenate two list in following
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]  output : ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
"""
def concate(list1,list2):
    list3 = [x + y for x in list1 for y in list2]
    print(list3)

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
concate(list1,list2)
