#Power Calculator

def Power(base,pow):                                           # function declaration
    power = base ** pow                                        # calculate power of base
    return power
base=int(input("Enter the base value"))
pow=int(input('Enter the power '))
print(f'The power of {base} and {pow} is:',Power(base,pow))    # function call in print statement
