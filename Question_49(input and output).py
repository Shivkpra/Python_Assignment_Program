"""Concatenate two list in following
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]  output : ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
"""
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3=[x+y for x in list1 for y in list2]
print(list3)
list3=[list1[0]+list2[0],list1[0]+list2[1],list1[1]+list2[0],list1[1]+list2[1]]
print(list3)
for i in list1:
    for j in list2:
        j=i+j
list3.append(j)
print(list(set(list3)))


