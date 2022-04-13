#String to Integer and Vice Versa


class convert:
  def __init__(self,a,b):
      self.a=a
      self.b=b


  def Convert(self,a,b):
      c = int(a)
      print(c)
      print(type(c))
      d = str(b)
      print(d)
      print(type(d))

a = input("Enter the string")
b = int(input("Enter the integer"))
obj=convert(a,b)
obj.Convert(a,b)
