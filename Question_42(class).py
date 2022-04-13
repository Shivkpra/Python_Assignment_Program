#Write a function to replace word with another word and another function to replace only alphabet

class replace:
    def __init__(self,string):
        self.string=string

    def replace_word(self,string):
        print(string)
        print(string.replace('Shiv', 'SHIV'))


    def replace_alphabate(self,string):
        print(string)
        print(string.replace('p', "P"))

string = 'Shiv Kumar prasad'
obj=replace(string)
obj.replace_word(string)
obj.replace_alphabate(string)
