#Modify the tuple

def modify(tou):
    L = list(tou)
    print(L)
    name = input("Enter the name to append in list")
    L.append(name)
    print(L)
    index = int(input("enter the value to remove from list"))
    if index in L:
        print("Present")
        L.pop(index)
        print(L)
    else:
        print(f"{index} is out of index")

tou=(1,2,3,4,5,6)
modify(tou)

