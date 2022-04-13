# Return the Remainder from Two Numbers

def reminder(num,den):                                               #function declaration
    if (den == 0):                                                   # check that den is equal to 0 or not
        print("Enter the denominator value greater than zero ")

    rem = num % den                                                  #calculate the remindar
    return rem
num = int(input('Enter the  positive numerator'))
den = int(input('Enter the  positive denominator'))

print(f"Th reminder of {num} and {den} is:",reminder(num,den))      #function call in print statement

