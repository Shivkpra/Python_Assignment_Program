"""Create a function that returns the sum of missing numbers.
sumMissingNumbers([1, 3, 5, 7, 10]) ➞ 29
// 2 + 4 + 6 + 8 + 9
"""

class missingNubmer:
    def __init__(self,l):
        self.l=l

    def missing_sum(self,l):
        s = 0
        sum_list = 0
        for i in range(1, 11):
            s = s + i

        for i in l:
            sum_list = sum_list + i

        print("The sum of the missing number is  :", s - sum_list)

l = [1, 3, 5, 7, 10]
obj=missingNubmer(l)
obj.missing_sum(l)
