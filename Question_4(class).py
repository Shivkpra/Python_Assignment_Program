# Return the Remainder from Two Numbers

class rem:                                                    #creating class
  def __init__(self,num,den):                                 #constructor
    self.num=num
    self.den=den

  def reminder(self,num,den):                                #function declaration
      if (den == 0):  # check that den is equal to 0 or not
          print("Enter the denominator value greater than zero ")

      rem = num % den                                        #calculating remindar
      print(rem)

num = int(input('Enter the positive  numerator'))
den = int(input('Enter the  positive denominator'))

obj = rem(num,den)                                           # creating object to access class
obj.reminder(num,den)
