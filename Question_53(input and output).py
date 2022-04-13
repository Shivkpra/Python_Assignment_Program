#Remove repetitive elements from the list, list length should be 25 include number, char etc

list=['shiv',2 ,78,90,12.9,"kumar",45.0,23,'a','b','n','m','z',26,89.5,65,"prasad",59,82,'y','z','m','r','j','h',90,41,47,
      82,97]

num=[]
n=int(input("how many number you want to delete from list"))
for i in range (0,n):
    i=int(input("Enter the index not greater than 25:"))
    num.append(i)
for i in num:
    list.pop(i)
    print(list)

