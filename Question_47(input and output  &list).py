"""Count Occurance of each element from list
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
"""

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print(sample_list)
cout_list=[]
for i in sample_list:
    cout=0
    j=i+1
    for j in sample_list:
        if i==j:
            cout+=1                                                  #increment the value of cout if element is repeated



    print(cout,end=" ")

