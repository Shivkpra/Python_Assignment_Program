'''Check if objOne Is Equal to objTwo
Create a function that checks to see if two object arguments are equal to one another. Return True if the objects are equal, otherwise, return False.
'''

def campare(a,b):
    if (a==b):
        return True
    else:
        return False
a = input("Enter the first string")
b = input("Enter the second string")
print(campare(a,b))
