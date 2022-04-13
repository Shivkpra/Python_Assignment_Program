# Covert hours into second
hr = int(input("Enter the hours"))
if (hr>24):                                # check whether the hr is less than  or not
    print("Invalid input")
else:
    sec = hr*60*60                        # covert hours into seconds
    print(f"In {hr} hours {sec}  seconds are  present")


