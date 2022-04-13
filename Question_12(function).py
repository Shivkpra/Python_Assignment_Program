# Convert Hours and Minutes into Seconds


def seconds(hr ,min):
    if (hr <= 24):
        hour = hr * 60 * 60;
    else:
        print("invalid value")

    if (min <= 30):
        minutes = min * 60
    else:
        print('invalid value')
    second = hour + minutes
    return second

min = int(input('Enter the mintues'))
hr = int(input('Enter the hours'))
print("total seconds are",seconds(hr,min))   # function  call in  print statement