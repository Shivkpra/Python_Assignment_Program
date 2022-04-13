"""Create a function that returns the sum of missing numbers.
sumMissingNumbers([1, 3, 5, 7, 10]) ➞ 29
// 2 + 4 + 6 + 8 + 9
"""
def missing_sum(l):
    s=0
    sum_list=0
    for i in range (1,11):
        s=s+i

    for i in l:
        sum_list=sum_list+i

    print("The sum of the missing number is  :",s-sum_list)

l=[1, 3, 5, 7, 10]
missing_sum(l)







