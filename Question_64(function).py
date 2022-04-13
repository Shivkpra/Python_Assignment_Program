#Write a program to print the sum of the polygon angle side in degree . Take side of angle input from console

def sum(n):
    if (n < 3):
        return 0
    return ((n - 2) * 180)



n=int(input("Enter the number of sides of polygon :"))
print("The sum of angle of polygon is :",sum(n))
