#Reverse the tuple

class revers_e:
    def __init__(self,tuples):
        self.tuples=tuples
    def reverse(self,tuples):
        new_tuple = tuples[::-1]
        print(new_tuple)

tuples = (10, 11, 12, 13, 14, 15)
obj=revers_e(tuples)
obj.reverse(tuples)

