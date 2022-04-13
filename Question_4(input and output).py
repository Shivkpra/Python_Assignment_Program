# Return the Remainder from Two Numbers

num = int(input('Enter the positive  numerator'))
den = int(input('Enter the  positive denominator'))
if (den==0):                                                                 # check that den is equal to 0 or not
    print("Enter the denominator value greater than zero ")
rem = num % den                                                              #calculate the remindar
print(f"Th reminder of {num} and {den} is:",rem)



