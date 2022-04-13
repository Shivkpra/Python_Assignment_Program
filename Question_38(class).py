class operato_r:
    def __init__(self,num1,num2):
        self.num1= num1
        self.num2=num2

    def fun(self,num1, num2):
        if operator == '+':
            print("Addition", num1 + num2)
        elif operator == '-':
            print("Subtraction", num1 - num2)
        elif operator == '*':
            print("Muitiplication", num1 * num2)
        elif operator == '/':
            if num2 == 0:
                print("the number should not be Zero")
            elif num2 == 1:
                print("Divsion", num1)
            else:
                print("Division", num1 / num2)
        elif operator == '%':
            if num2 == 0:
                print("the number should not be Zero")
            elif num2 == 1:
                print("reminder", num1)
            else:
                print("reminder", num1 % num2)

num1 = int(input("Enter the first number  :"))
num2 = int(input("Enter the second number  :"))
operator = input("Enter the operator")
obj=operato_r(num1,num2)
obj.fun(num1, num2)