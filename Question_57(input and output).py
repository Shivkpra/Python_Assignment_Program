#Calculate the date 7 month from any date, take date input from console

import datetime
year = int(input('Enter a year'))
month = int(input('Enter a month'))
day = int(input('Enter a day'))

date1 = datetime.date(year, month, day)
print(date1)

current_date=datetime.date(year, month, day)+datetime.timedelta(days=30*7)
print(current_date)
