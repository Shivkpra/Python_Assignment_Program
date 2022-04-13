#Write a program to print the sum of the polygon angle side in degree . Take side of angle input from console

n=int(input("Enter the sides of polygon  :"))
if (n<3):
    print(" Not a ploygon")
else:
    sum=(n - 2) * 180
    print("The sum of the angle of polygon is :",sum)
