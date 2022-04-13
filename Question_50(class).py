#Take two list and Iterate both list simultaneously and print output

class twolis_t:
    def __init__(self,list_1,list_2):
        self.list_1=list_1
        self.list_2=list_2

    def two_list(self,list_1, list_2):
        for (i, j) in zip(list_1, list_2):
            print("i: ", i, "; j: ", j)

list_1 = [1, 2, 3, 4, 5, ]
list_2 = ['a', 'b', 'c', 'd', 'e']
obj=twolis_t(list_1,list_2)
obj.two_list(list_1, list_2)
