class sortin_g:
    def __init__(self,list):
        self.list=list

    def sorting(self,list):
        for i in range(len(list)):
            for j in range(i + 1, len(list)):

                if list[i] > list[j]:
                    list[i], list[j] = list[j], list[i]

        print(list)

list = []
n = int(input("Enter the number of elements :"))
for i in range(n):
    i = input(f'Enter the value {i}:')
    list.append(i)
obj=sortin_g(list)
obj.sorting(list)
