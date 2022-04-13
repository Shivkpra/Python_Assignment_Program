#Find the day of the week from given date , dae input from console
import datetime
week_days= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
l=list(map(int, input("Enter date eg: 2019/05/05").split('/')))
day=datetime.date(l[0],l[1],l[2]).weekday()
print(week_days[day])