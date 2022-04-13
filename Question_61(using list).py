#Get only unique items from dictionary

dic={1:"shiv",2:"kumar",3:"prasad", 4:"shiv",5:"kumar",6:"prasad"}
list =[]
for val in (dic.values()):
  if val in list:
    continue
  else:
    list.append(val)

print (list)
