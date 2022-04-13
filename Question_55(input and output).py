#Calculate no of days between two date , take input from console
from datetime import date
year = int(input('Enter a year'))
month = int(input('Enter a month'))
day = int(input('Enter a day'))
date_1= date (year,month,day)
print(date_1)
year_2 = int(input('Enter a year'))
month_2= int(input('Enter a month'))
day_2 = int(input('Enter a day'))
date_2=date(year_2,month_2,day_2)
print(date_2)
delta=date_1-date_2
print(delta.days)
from datetime import date
f_date = date(2014, 7, 1)
l_date = date(2014, 9,1 )
delta = l_date - f_date
print(delta.days)

