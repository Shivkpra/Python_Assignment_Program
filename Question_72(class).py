# Check if given char is vowel or consonant

import re
class cha_r:
    def __init__(self,vowel_list,ch):
        self.ch=ch
        self.vowel_list=vowel_list

    def char(self,vowel_list,ch):
        if re.search("[a-z]", ch) or re.search("[A-Z]", ch):
            if ch in vowel_list:
                print(ch, "vowel")
            else:
                print(ch, "Consonat")
        else:
            print("Invalid  input")

vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
ch = input("Enter the chracter :")
obj=cha_r(vowel_list,ch)
obj.char(vowel_list,ch)
