'''Define a class/function which has at least two methods: getString: to get a string from console input printString:
to print the string in upper case.'''

class uppe_r:
    def __init__(self):
        self.s=""
    def getstring(self):
        self.s=input("Enter the string:")
    def printstring(self):
        result = ''
        for char in self.s:
            if ord(char) >= 65:
                result += chr(ord(char) - 32)
        print(result)


obj=uppe_r()
obj.getstring()
obj.printstring()
