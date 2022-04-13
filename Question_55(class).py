#Calculate no of days between two date , take input from console

from datetime import date
class datetim_e:
    def __init__(self,l_date,f_date):
        self.l_date=l_date
        self.f_date=f_date

    def date_time(self,l_date, f_date):
        delta = l_date - f_date
        print(delta.days)

f_date = date(2014, 7, 1)
l_date = date(2014, 8, 1)
obj=datetim_e(l_date,f_date)
obj.date_time(l_date, f_date)
