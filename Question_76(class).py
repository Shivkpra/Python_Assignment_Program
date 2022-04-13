#Write a function that returns the least common multiple (LCM) of two integers.

class lc_m:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def Lcm(self,num1, num2):

        if num1 > num2:
            largest = num1
        else:
            largest = num2

        while (True):
            if ((largest % num1 == 0) and (largest % num2 == 0)):
                lcm = largest
                break
            largest += 1

        return lcm

num1 = int(input("Enter the number  :"))
num2 = int(input("Enter the number :"))
obj=lc_m(num1,num2)
print("The L.C.M. is", obj.Lcm(num1, num2))