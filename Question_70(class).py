class palidrom_e:
    def __init__(self,num):
        self.num=num

    def palidrome(self,num):
        n = num
        s = 0
        while (n > 0):
            rem = n % 10
            s = s * 10 + rem
            n = n // 10
        if num == s:
            print("The number is palidrome number")
        else:
            print("The number is not a palidrome number")

num = int(input("Enter the number:"))
obj=palidrom_e(num)
obj.palidrome(num)
