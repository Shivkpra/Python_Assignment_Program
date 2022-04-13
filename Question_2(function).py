def add_number(a,b):                                        #function  delaration
    c = a + b                                               # calculate the sum of a and b
    return c
a = int(input("Enter the value of first number"))
b = int(input("Enter the value of second number"))
print(f"The sum of {a} and {b} is ",add_number(a,b))        # function call in print statement