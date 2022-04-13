#Power Calculator

b=int(input("Enter the base value"))
e=int(input('Enter the power '))
power=1
for i in range (e):
    power=power*b                                      # multiple with power untill the power is not greater than e
print(power)

