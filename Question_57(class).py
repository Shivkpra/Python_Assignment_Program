#Calculate the date 7 month from any date, take date input from console

import datetime
class nextdat_e:
    def __init__(self,year,month,days):
        self.year=year
        self.month=month
        self.day=day
    def  next_date(self,year,month,day):
        date1 = datetime.date(year, month, day)
        print(date1)
        current_date = datetime.date(year, month, day) + datetime.timedelta(days=30 * 7)
        print(current_date)


year = int(input('Enter a year'))
month = int(input('Enter a month'))
day = int(input('Enter a day'))
obj=nextdat_e(year,month,day)
obj.next_date(year, month, day)
