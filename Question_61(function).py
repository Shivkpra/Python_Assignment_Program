#Get only unique items from dictionary

def unquie(dic):
    s = set(dic.values())
    print(s)


dic={1:"shiv",2:"kumar",3:"prasad", 4:"shiv",5:"kumar",6:"prasad"}
unquie(dic)

