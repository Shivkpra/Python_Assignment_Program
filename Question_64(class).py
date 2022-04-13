#Write a program to print the sum of the polygon angle side in degree . Take side of angle input from console
class polygon:
    def __init__(self,n):
        self.n=n

    def sum(self,n):
        if (n<3):
            return 0
        return ((n-2) * 180)

n = int(input("Enter the number of sides of polygon :"))
obj=polygon(n)
print("The sum of angle of polygon is :", obj.sum(n))
