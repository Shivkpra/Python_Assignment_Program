'''The Farm Problem
In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:
chickens = 2 legs
cows = 4 legs
pigs = 4 legs
The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a function that returns the total number of legs of all the animals.
'''

chickens_num=int(input('Enter the  number of chickens in farm'))
cows_num=int(input('Enter the  number of cows in farm'))
pigs_num=int(input('Enter the  number of pig in farm'))
chickens_legs=chickens_num* 2
cows_legs=cows_num* 4
pigs_legs=pigs_num* 4
total_legs=chickens_legs+cows_legs+pigs_legs                                  # calculating legs of animal in farm 
print('Total legs of the animal which are present in farm is',total_legs)
