#write a program which accepts a string from the console and print it in reverse order.
string=input("Enter the string : " )
reverse=''
for i in string:
    reverse=i+reverse
print(reverse)