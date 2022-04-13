"""Create a function that takes two dates and returns the number of days between the first and second date."""
from datetime import date
year1=int(input("Enter the year"))
month1=int(input("Enter the month"))
day1=int(input("Enter the day"))
year2=int(input("Enter the year"))
month2=int(input("Enter the month"))
day2=int(input("Enter the month"))

f_date = date(year1,month1,day1)
l_date = date(year1,month2,day2)
delta = l_date - f_date
print("days:",delta.days)