"""write a program to sort the data by ascending and descending order
Take list of data - you can take input from console or define list
"""
def asc_desc(l):
    l.sort()
    print("ascending oder",l)
    print("desending oder",l[:: -1])




l=[]
n=int(input("Enter the number of elements:"))
for i in range (n):
    i=int(input(f"enter the value {i}  :"))
    l.append(i)
asc_desc(l)