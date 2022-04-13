#write a program which accepts a string from the console and print it in reverse order.

class revers_e:
     def __init__(self,string):
         self.string=string
     def reverse(self,string):
         reverse=''
         for i in string:
             reverse=i+reverse
         print(reverse)

string=input("Enter the string : " )
obj=revers_e(string)
obj.reverse(string)