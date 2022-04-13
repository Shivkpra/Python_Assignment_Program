# Covert hours into second

class Second:                                                      # creating class
  def __init__(self,hr):                                           #constructor (it call the object)
    self.hr=hr

  def second(self,hr):                                             # function declaration
      if (hr > 24):                                                #check whether the hr is less than  or not
          print("Invalid input")
      else:
          sec = hr * 60 * 60                                       #convert hours into second
          print(f"In {hr} hours {sec}  seconds are  present")

hr=int(input('Enter the hours:'))

obj = Second(hr)                                                   #creating object (to access the object and function of class)
obj. second(hr)

