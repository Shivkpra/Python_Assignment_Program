"""Concatenate two list in following
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]  output : ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
"""

class concat_e:
    def __init__(self,list1,list2):
        self.list1=list1
        self.list2=list2

    def concate(self,list1, list2):
        list3 = [x + y for x in list1 for y in list2]
        print(list3)
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
obj=concat_e(list1,list2)
obj.concate(list1, list2)
