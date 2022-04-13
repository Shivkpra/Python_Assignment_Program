#Given the month and year as numbers, return whether that month contains a Friday 13th.
from datetime import date

class day:
    def __init__(self,month,year):
        self.year=year
        self.month=month

    def test(self,month, year):
        return str(date(year, month, 13).strftime("%A") == 'Friday')

month = 5
year = 2022;
print("Month No.: ", month, " Year: ", year);
obj=day(month,year)
print("Check whether the said month and year contains a Monday 13th.: ", obj.test(month, year));
