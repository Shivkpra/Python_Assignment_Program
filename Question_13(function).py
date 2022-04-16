#String to Integer and Vice Versa

def type_coversion(a,b):            #function declaration
    c = int(a)
    print(c)
    print(type(c))                  #type of c is print
    d=str(b)
    print(d)
    print(type(d))                  #type of d is print            
a=input("Enter the string")
b=int(input("Enter the integer"))
type_coversion(a,b)                  #function call
