#Write a program to perform all basic mathematical operations
num1=int(input("Enter the first number  :"))
num2=int(input("Enter the second number  :"))
operator=input("Enter the operator")
if operator=='+':
    print("Addition",num1+num2)
elif operator=='-':
    print("Subtraction",num1-num2)
elif  operator=='*':
    print("Muitiplication",num1*num2)
elif operator=='/':
    if num2==0:
        print("the number should not be Zero")
    elif num2==1:
        print("Divsion",num1)
    else:
        print("Division",num1/num2)
elif operator=='%':
    if num2==0:
        print("the number should not be Zero")
    elif num2==1:
        print("reminder",num1)
    else:
        print("reminder",num1%num2)