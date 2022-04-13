# Convert list into dictionary and add new item into dictionary

list=[]
n=int(input("PLease enter even value"))
for i in range (n):
    i=int(input("Enter the value"))
    list.append(i)
res_dct = {list[i]: list[i + 1] for i in range(0, len(list), 2)}
print(res_dct)
res_dct["name "] = "shiv"
print(res_dct)

