# Convert Hours and Minutes into Seconds

class seconds:                                     #creating class
  def __init__(self,hr,min):                       #construtor
      self.hr=hr
      self.min=min


  def convert(self,hr, min):                       #function declaration
      if (hr <= 24):                               #check hr is less than 24  or not
          hour = hr * 60 * 60;                     #converting hr in second
      else:
          print("invalid value")

      if (min <= 30):                              #check min is less than 30 or not
          minutes = min * 60                       #converting min in second
      else:
          print('invalid value')
      second = hour + minutes                      # sum of all second                
      return second

min = int(input('Enter the mintues'))
hr = int(input('Enter the hours'))
obj=seconds(hr,min)                                # creating object for  class
print("total seconds are", obj.convert(hr, min))
