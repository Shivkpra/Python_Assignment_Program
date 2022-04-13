class lengh_t:
    def __init__(self,num):
        self.num=num
    def lenght(self,num):
        cout=0

        while(num>0):
            num=num//10
            cout+=1
        print("The digits present in this number is :",cout)

num=int(input("Enter the number :"))
obj=lengh_t(num)
obj.lenght(num)