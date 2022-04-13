# Return the First Element in a List

class First:                                               # creating class
  def __init__(self,L):                                    #constructor
      self.L=L

  def list_first(self, L):                                 #function declaration
      print(L[0])


n=int(input('Enter the  number of elements'))
L=[]
for i in range(n):                                         #use loop of append the elements in list
    i=int(input("Enter the value "))
    L.append(i)

obj=First(L)                                               # creating object to access class
print("First value of the ;list is:",obj.list_first(L))

