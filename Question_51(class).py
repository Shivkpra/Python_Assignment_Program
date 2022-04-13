#Extend nested list by adding sub list with specific index taken from console

class inde_x:
    def __init__(self,list,list_1):
        self.list=list
        self.list_1=list_1

    def index(self,list, list_1):
        list.extend([list_1])
        print(list)
        l1 = int(input("Enter the index of main list"))
        l2 = int(input("Enter the index for nested list"))
        print(list[l1][l2])

list = [[10, 56, 78, 92], ['a', 'b', 'c', 'd']]
list_1 = ["shiv", "kumar", "prasad"]
obj=inde_x(list,list_1)
obj.index(list, list_1)
