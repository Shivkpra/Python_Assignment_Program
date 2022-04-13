#Reverse the tuple

tuples = (10, 11, 12, 13, 14, 15)
new_tuple=tuples[::-1]
print(new_tuple)

tuples = (10, 11, 12, 13, 14, 15)
new_tuple=()
for i in reversed(tuples):
    new_tuple=new_tuple + (i,)
print(new_tuple)



