"""Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
Example : 2 cats and 3 dogs.
Output should be :
['2', '3']
[‘cats’, ‘dogs’]
"""
class concat_e:
    def __init__(self,l1,l2):
        self.l1=l1
        self.l2=l2
    def concate(self,l1,l2):
        l3=[i+j for i,j in zip(l1,l2)]
        print(l3)

l1=['2 ', '3 ']
l2=['cats','dogs']
obj=concat_e(l1,l2)
obj.concate(l1,l2)