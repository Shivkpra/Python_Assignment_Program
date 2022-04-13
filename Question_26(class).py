'''Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5. The numbers obtained should be printed in a comma-separated sequence on a single line.
You can take any range like 2000-4700 or 3800-4900 etc '''
class ranges:
    def __init__(self,first,last):
        self.first=first
        self.last=last

    def value(self,first, last):
        for i in range(first, last):
            if i % 7 == 0 and i % 5 != 0:
                print(i, end=",")

first = int(input("Enter the starting value "))
last = int(input("Enter the last value"))
obj=ranges(first,last)
obj.value(first, last)
