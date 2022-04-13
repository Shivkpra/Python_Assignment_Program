# Check if key exists in dictionary and delete that key value from dictionary

dict_1 = {"a": 1, "b":2, "c":3,"d":4,"e":5,"f":6,"g":7}
if "a" in dict_1:
    print("Exists")
else:
    print("Does not exist")
dict_1.pop("a", None)
print(dict_1)

