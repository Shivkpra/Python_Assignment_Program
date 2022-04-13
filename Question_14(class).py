'''Check if objOne Is Equal to objTwo
Create a function that checks to see if two object arguments are equal to one another. Return True if the objects are equal, otherwise, return False.
'''

class compare_string:
  def __init__(self,a,b):
      self.a=a
      self.b=b


  def compare(self,a,b):
      if (a == b):
          print(True)
      else:
          print(False)

a = input("Enter the first string")
b = input("Enter the second string")
obj=compare_string(a,b)
obj.compare(a,b)
