class add:                                                    # creating class
  def __init__(self,a,b):                                     # constuctor
    self.a=a
    self.b=b
  def add_number( self,a, b):                                 #function declaration
          c = a + b                                           #calculate sum of a and b
          print(f"The sum of {a} and {b} is {c} ")

a = int(input("Enter the value of first number"))
b = int(input("Enter the value of second number"))
obj = add(a,b)                                                # creating object(which can able to access object and function of class)
obj. add_number(a,b)

