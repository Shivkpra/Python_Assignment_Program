# Convert Age to Days
def age(year,month,days):                                         # function declaration
    year_days = year * 365                                        # convert year in to days
    if (month < 12):                                               # check value of month is less than 12 or not
        month_days = month * 30;                                  # convert month in days
    else:
        print("invalid value")
    Days = year_days + month_days + days                          # sum of all days of year and month
    return Days
year=int(input("Enter the year of age"))
month=int(input('Enter the month of age'))
days=int(input('Enter the days of age'))

print("The of the person in days: ",age(year,month,days))               #function call in print stetemment
