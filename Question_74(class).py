"""Create a function that takes an array of strings and returns an array with only the strings that have numbers in
them. If there are no strings containing numbers, return an empty array.
"""

import re
class strin_g:
    def __init__(self,arr):
        self.arr=arr

    def string(self,arr):
        print(arr)
        for i in arr:
            if re.search("[0-9]", i):
                print(i)
            else:
                print("Empty string")

arr = ["dog", "123", "rush", "678", "107", "234"]
obj=strin_g(arr)
obj.string(arr)
