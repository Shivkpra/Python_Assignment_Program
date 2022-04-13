''''Write a program that accepts a comma separated sequence of words as input and prints the words in a
comma-separated sequence after sorting them alphabetically.
'''

list = []
n=int(input("Enter the number of elements :"))
for i in range (n):
    i=input(f'Enter the value {i}:')
    list.append(i)
for i in range(len(list)):
    for j in range(i + 1, len(list)):

        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]

print(list)
