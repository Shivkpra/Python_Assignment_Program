"""Define a function that can accept two strings as input and print the string with maximum length in the console.
If two strings have the same length, then the function should print all strings line by line.
"""
def fun(str1,str2):
    cout=0
    for i in str1:
        cout+=1
    cout_1=0
    for i in str2:
        cout_1+=1
    if cout==cout_1:
        print("The stings are line by line")
    elif cout > cout_1:
        print("Maximum length",str1)
    else:
        print("Maximum length",str2)

str1=input("Enter the  first string:")
str2=input("Enter the second string")
fun(str1,str2)