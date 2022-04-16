# Return a String as an Integer

class coversion:                                             # creating class
  def __init__(self,string):                                 #constructor
      self.string=string


  def type_conversion( self,string):                         # function declaration
      print(int(string))                                     # Return a String as an Integer
                # convert the string in integer
      print(type(int(string)))                               #print the type of string


string = input("Enter the string")
obj = coversion(string)                                      # creating object to access the class
obj.type_conversion(string)

