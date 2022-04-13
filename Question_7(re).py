#Power Calculator

def power(base,pow):                               #function declaration
    if pow==0:
        return 0
    elif pow==1:
        return base
    else:
        return(base*power(base,pow-1))             # calling function in function
base=int(input("Enter the base value"))
pow=int(input('Enter the power '))
print(power(base,pow))                             # function call

