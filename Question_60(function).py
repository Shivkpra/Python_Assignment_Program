# Check if key exists in dictionary and delete that key value from dictionary

def exists(dict_1):
    if "e" in dict_1:
        print("Exists")
    else:
        print("Does not exist")
    dict_1.pop("e", None)
    print(dict_1)

dict_1 = {"a": 1, "b":2, "c":3,"d":4,"e":5,"f":6,"g":7}
exists(dict_1)
