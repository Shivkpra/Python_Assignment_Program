# Convert Age to Days

year=int(input("Enter the year of age"))
month=int(input('Enter the month of age'))
days=int(input('Enter the days of age'))
year_days=year*365                                            # covert year into days
if (month<12):                                                # checking month is less than 12 or not
    month_days=month*30;                                      # coverting month in days
else:
    print("invalid value")
Days=year_days+month_days+days                                 # sum of all days
print("The of the person in days ",Days)
