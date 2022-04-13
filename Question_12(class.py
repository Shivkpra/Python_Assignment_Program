# Convert Hours and Minutes into Seconds

class seconds:
  def __init__(self,hr,min):
      self.hr=hr
      self.min=min


  def convert(self,hr, min):
      if (hr <= 24):
          hour = hr * 60 * 60;
      else:
          print("invalid value")

      if (min <= 30):
          minutes = min * 60
      else:
          print('invalid value')
      second = hour + minutes
      return second

min = int(input('Enter the mintues'))
hr = int(input('Enter the hours'))
obj=seconds(hr,min)                           # creating object for  class
print("total seconds are", obj.convert(hr, min))
