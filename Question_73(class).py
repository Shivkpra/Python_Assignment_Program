"""Create a function that takes two dates and returns the number of days between the first and second date."""
from datetime import date
class differ:
    def __init__(self,f_date,l_date):
        self.f_date=f_date
        self.l_date=l_date

    def Date(self,f_date, l_date):
        delta = l_date - f_date
        print("days:", delta.days)

year1 = int(input("Enter the year"))
month1 = int(input("Enter the month"))
day1 = int(input("Enter the day"))
year2 = int(input("Enter the year"))
month2 = int(input("Enter the month"))
day2 = int(input("Enter the month"))

f_date = date(year1, month1, day1)
l_date = date(year1, month2, day2)
obj=differ(f_date,l_date)
obj.Date(f_date, l_date)
