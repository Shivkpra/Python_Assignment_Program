#Given the month and year as numbers, return whether that month contains a Friday 13th.

from datetime import date
def test(month, year):
    return str(date(year,month,13).strftime("%A")=='Friday')

month = 5;
year = 2022;
print("Month No.: ", month, " Year: ", year);
print("Check whether the said month and year contains a Monday 13th.: " , test(month, year));
