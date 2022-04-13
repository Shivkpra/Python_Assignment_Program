"""write a program to sort the data by ascending and descending order
Take list of data - you can take input from console or define list
"""

l = [67, 21, 72, 42, 711, 18,27,442,38,172, 43, 32]
cout=0
for i in l:
    cout+=1
for i in range(cout):
    for j in range(i + 1, cout):

        if l[i] > l[j]:
           l[i], l[j] = l[j], l[i]

print ("ascending oder:",l)

l = [62, 35, 12, 22, 11, 34,22,45,3,127, 63, 384]
cout=0
for i in l:
    cout+=1


for i in range(cout):
    for j in range(i + 1, cout):

        if l[i] < l[j]:
           l[i], l[j] = l[j], l[i]

print ("descending oder:",l)

