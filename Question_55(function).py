#Calculate no of days between two date , take input from console

from datetime import date
def date_time(l_date,f_date):
    delta = l_date - f_date
    print(delta.days)

f_date = date(2014, 7, 1)
l_date = date(2014, 10,1 )
date_time(l_date,f_date)
