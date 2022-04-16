#String to Integer and Vice Versa


class convert:                                    #creating class
  def __init__(self,a,b):                         #constructor
      self.a=a
      self.b=b


  def Convert(self,a,b):                         #function declaration
      c = int(a)
      print(c)
      print(type(c))                             #type of c is printed
      d = str(b)
      print(d)
      print(type(d))                             #type of d is printed 

a = input("Enter the string")
b = int(input("Enter the integer"))
obj=convert(a,b)                                 #creating object for class
obj.Convert(a,b)
