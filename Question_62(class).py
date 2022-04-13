#Return new set of identical items from two sets

class inter_section:
    def __int__(self,set_1,set_2):
        self.set_1=set_1
        self.set_2=set_2

    def inter(self,set_1, set_2):
        print(set_1.intersection(set_2))

set_1 = {10, 30, 40, 50, 80, 67, 89, 78, 45, 23}
set_2 = {56, 78, 67, 45, 87, 19, 97, 64}
obj=inter_section()
obj.inter(set_1, set_2)


