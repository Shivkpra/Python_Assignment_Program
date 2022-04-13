"""Given a string, reverse all the words which have odd length. The even length words are not changed."""
def reverse_odd(string):
    print(string)
    cout = -1
    index = []
    odd = []
    even = []
    str = ''
    for i in string:
        cout += 1
        index.append(cout)
    for i in index:
        if i % 2 != 0:
            odd.append(string[i])
        else:
            even.append(string[i])
    final = [i + j for i, j in zip(even, odd[::-1])]

    for i in final:
        str = str + i

    str = str + even[-1]
    print(str)
    print(odd)



string=input("Enter the string (string must be a contain even words):")
reverse_odd(string)