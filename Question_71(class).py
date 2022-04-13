# Check char is digit without using isdigit() , take input from console
import re
class char:
    def __init__(self,string):
        self.string=string

    def char_digit(self,string):

        if re.search("[a-z]", string):
            print(False)
        elif re.search("[A-Z]", string):
            print(False)
        elif re.search("[$#@]", string):
            print(False)
        elif re.search("\s", string):
            print(False)
        else:
            print(True)

string = input("Enter the string :")
obj=char(string)
obj.char_digit(string)