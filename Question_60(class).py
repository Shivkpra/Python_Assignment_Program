# Check if key exists in dictionary and delete that key value from dictionary

class exist_s:
    def __init__(self,dict_1):
        self.dict_1=dict_1

    def exists(self,dict_1):
        if "u" in dict_1:
            print("Exists")
        else:
            print("Does not exist")
        dict_1.pop("u", None)
        print(dict_1)

dict_1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7}
obj=exist_s(dict_1)
obj.exists(dict_1)
