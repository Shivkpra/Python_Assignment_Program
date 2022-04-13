"""Write a program that accepts a sentence and calculate the number of letters and digits and also calculates the
upper and lower case letters
"""
def cout(str):
    letter = 0
    digit = 0
    upper = 0
    lower = 0
    for i in str:
        if (i >= 'a' or i <= 'z') and (i >= 'A' or i <= 'Z'):
            if i.isspace() != True:
                letter += 1

        if (i >= '0' and i <= '9'):
            digit += 1

        if i.isupper() == True:
            upper += 1

        if i.islower() == True:
            lower += 1
    print("Total number of letter", letter - digit)
    print("Total number of digits", digit)
    print("Total number of Upper", upper)
    print("Total number of lower", lower)


str=input("enter the string:")
cout(str)
