#Extend nested list by adding sub list with specific index taken from console

def index(list,list_1):
    list.extend([list_1])
    print(list)
    l1 = int(input("Enter the index of main list"))
    l2 = int(input("Enter the index for nested list"))
    print(list[l1][l2])

list=[[10,56,78,92],['a','b','c','d']]
list_1=["shiv","kumar","prasad"]
index(list,list_1)
