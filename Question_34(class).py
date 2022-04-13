"""write a program to sort the data by ascending and descending order
Take list of data - you can take input from console or define list
"""
class ascdes_c:
    def __init__(self,l):
        self.l=l
    def asc_desc(self,l):
        cout = 0
        for i in l:
            cout += 1
        for i in range(cout):
            for j in range(i + 1, cout):

                if l[i] > l[j]:
                    l[i], l[j] = l[j], l[i]

        print("ascending oder:", l)

        cout = 0
        for i in l:
            cout += 1

        for i in range(cout):
            for j in range(i + 1, cout):

                if l[i] < l[j]:
                    l[i], l[j] = l[j], l[i]

        print("descending oder:", l)

l = [62, 35, 12, 22, 11, 34, 22, 45, 3, 127, 63, 384]

obj=ascdes_c(l)
obj.asc_desc(l)