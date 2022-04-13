#Power Calculator

class power:                                   # creating class
  def __init__(self,b,e):                      # constructor
      self.b=b
      self.e=e

  def P(self,b, e):                              # function declaration
      if e == 0:
          return 0
      elif e == 1:
          return b
      else:
          return b**e                            #return the  power of b

b = int(input("Enter the base value"))
e= int(input('Enter the power '))
obj=power(b,e)                                   #creating  object to access class
print("POWER",obj.P(b,e))
