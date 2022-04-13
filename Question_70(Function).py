#7 Write a program to identify if number is palindrome or not
def palidrome(num):
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


num=int(input("Enter the number:"))
palidrome(num)
