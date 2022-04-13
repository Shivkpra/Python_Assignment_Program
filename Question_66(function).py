#Create a function that takes a number and returns its length(use of the len() function is prohibited)
def lenght(num):
    s=str(num)
    cout=0
    for i in s:
        cout+=1
    print("the length of the number is :",cout)

num=int(input("Enter the number  :"))
lenght(num)