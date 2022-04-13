#Take two list and Iterate both list simultaneously and print output

def two_list(list_1,list_2):
    for (i, j) in zip(list_1, list_2):
        print("i: ", i, "; j: ", j)

list_1=[1,2,3,4,5,]
list_2=['a','b','c','d','e']
two_list(list_1,list_2)

