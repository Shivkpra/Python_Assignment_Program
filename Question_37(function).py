"""Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
Example : 2 cats and 3 dogs.
Output should be :
['2', '3']
[‘cats’, ‘dogs’]
"""
def concate(l1,l2):
    l3=[i+j for i,j in zip(l1,l2)]
    print(l3)

l1=['2 ', '3 ']
l2=['cats','dogs']
concate(l1,l2)