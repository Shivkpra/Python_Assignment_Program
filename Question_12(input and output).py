# Convert Hours and Minutes into Seconds
hr=int(input('Enter the hours')) 
if(hr<=24):                                                #checking hr is less than 24 or not
    hour=hr*60*60;                                         #converting hr is second
else:
    print("invalid value")
min=int(input('Enter the mintues'))
if(min<=30):                                              #checking  min is less than 30 or not
    minutes=min*60                                        #converting min to second
else:
    print('invalid value')
seconds=hour+minutes                                      #sum of all seconds
print(f"In {hr} hours and {min} minutes have {seconds}")
