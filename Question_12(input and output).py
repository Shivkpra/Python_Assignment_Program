# Convert Hours and Minutes into Seconds
hr=int(input('Enter the hours'))
if(hr<=24):
    hour=hr*60*60;
else:
    print("invalid value")
min=int(input('Enter the mintues'))
if(min<=30):
    minutes=min*60
else:
    print('invalid value')
seconds=hour+minutes
print(f"In {hr} hours and {min} minutes have {seconds}")
