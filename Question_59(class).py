#Merge two dictionaries into one and rename dictionary key name


class merg_e:
    def __init__(self,dict1,dict2):
        self.dict1=dict1
        self.dict2=dict2

    def merge(self,dict1, dict2):
        dict1.update(dict2)
        print(dict1)
        dict1[1] = dict1.pop('a')
        dict1[2] = dict1.pop('b')
        dict1[3] = dict1.pop('c')
        dict1[4] = dict1.pop('d')
        print(dict1)

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
obj=merg_e(dict1,dict2)
obj.merge(dict1, dict2)
