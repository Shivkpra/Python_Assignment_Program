#Sort tuple by 2nd item tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

class sort:
    def __init__(self,tuple1):
        self.tuple1=tuple1
    def sorted(self,tuple1):
        tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
        print(tuple1)

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
obj=sort(tuple1)
obj.sorted(tuple1)



