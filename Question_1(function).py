# Covert hours into second

def second(hr):                                                      #function declaration
    if (hr > 24):                                                    #check whether the hr is less than  or not
        print("Invalid input")
    else:
        sec = hr * 60 * 60                                           # covert hours into seconds
        print(f"In {hr} hours {sec}  seconds are  present")
second(hr=3)                                                         #function call

