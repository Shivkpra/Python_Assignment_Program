# Convert Hours and Minutes into Seconds


def seconds(hr ,min):                                     #function declaration
    if (hr <= 24):                                        # checking hr is less than 24 or or not
        hour = hr * 60 * 60;                              #converting hr in seconds
    else:
        print("invalid value")

    if (min <= 30):                                       #checking min is less than 30 or not
        minutes = min * 60                                #converting min in seconds
    else:
        print('invalid value')
    second = hour + minutes                               #sum of all seconds
    return second

min = int(input('Enter the mintues'))
hr = int(input('Enter the hours'))
print("total seconds are",seconds(hr,min))               # function  call in  print statement
