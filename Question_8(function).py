# Boolean to String Conversion

def bool_string(x):                                  # function declaration
    a = x > 4 and x < 10
    print(a)
    print(type(a))
    s = str(a)                                        # converting boolean in str
    print(s)
    print(type(s))
x=int(input('Enter the value'))
bool_string(x)                                       # function call




