# Check char is digit without using isdigit() , take input from console

import re
string=input("Enter the string :")

if re.search("[a-z]",string):
    print(False)
elif re.search("[A-Z]",string):
    print(False)
elif re.search("[$#@]",string):
    print(False)
elif re.search("\s",string):
    print(False)
else:
    print(True)