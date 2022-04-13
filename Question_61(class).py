#Get only unique items from dictionary
class unqui_e():
    def __init__(self,dic):
        self.dic=dic
    def unquie(self,dic):
        list = []
        for val in (dic.values()):
            if val in list:
                continue
            else:
                list.append(val)

        print(list)

dic={1:"shiv",2:"kumar",3:"prasad", 4:"shiv",5:"kumar",6:"prasad"}
obj=unqui_e(dic)
obj.unquie(dic)
