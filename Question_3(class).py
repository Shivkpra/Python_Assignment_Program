# Return the Next Number from the Integer Passed

class Next:                                                   #creating class
  def __init__(self,n):                                       #constructor
    self.n=n

  def number(self,n):                                          #function call
    n = n + 1                                                  #it will increase value of n by 1
    print(n)

n = int(input('Enter the number'))
obj = Next(n)                                                 #creating object(to access the class object and function)
obj. number(n)
