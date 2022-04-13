#Find the day of the week from given date , dae input from console
import datetime
class week:
    def __init__(self,l):
        self.l=l

    def weekday(self,l):
        week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day = datetime.date(l[0], l[1], l[2]).weekday()
        print(week_days[day])


l=list(map(int, input("Enter date eg: 2019/05/18").split('/')))
obj=week(l)
obj.weekday(l)