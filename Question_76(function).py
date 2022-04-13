#Write a function that returns the least common multiple (LCM) of two integers.

def Lcm(num1, num2):

   if num1> num2:
       largest = num1
   else:
       largest = num2

   while(True):
       if((largest% num1 == 0) and (largest % num2 == 0)):
           lcm = largest
           break
       largest += 1

   return lcm

num1 = int(input("Enter the number  :"))
num2 = int(input("Enter the number :"))

print("The L.C.M. is", Lcm(num1, num2))