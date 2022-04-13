'''The Farm Problem
In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:
chickens = 2 legs
cows = 4 legs
pigs = 4 legs
The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a function that returns the total number of legs of all the animals.
'''

class Farm:
  def __init__(self,ch_num,co_num,pi_num):
      self.ch_num=ch_num
      self.co_num=co_num
      self.pi_num=pi_num

  def total_legs( self,ch, co, pi):
      ch_legs = ch_num * 2
      co_legs = co_num * 4
      pi_legs = pi_num * 4
      total_leg = ch_legs + co_legs + pi_legs
      return total_leg

ch_num = int(input('Enter the  number of chickens in farm'))
co_num = int(input('Enter the  number of cows in farm'))
pi_num = int(input('Enter the  number of pig in farm'))
obj=Farm(ch_num,co_num,pi_num)
print('Total legs of the animal which are present in farm is', obj.total_legs(ch_num, co_num, pi_num))
