"""Count Occurance of each element from list
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
"""

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print( sample_list)

cout=dict()
for item in sample_list:
    if item in cout:                                              #increment the value of cout if element is repeated
        cout[item] += 1
    else:
        cout[item] = 1                                           # cout value is remain 1 if no repeated element is found

print("Printing count of each item  ", cout)




