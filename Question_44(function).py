"""Create a list by picking an odd-index items from the first list and even index items from the second
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
Output
Element at odd-index positions from list one
[6, 12, 18]
Element at even-index positions from list two
[4, 12, 20, 28]

Printing Final third list
[6, 12, 18, 4, 12, 20, 28]
"""

def list(l1,l2):
    odd_index = []
    even_index = []
    cout_odd = -1
    odd_elemnet = []
    even_elemnet = []
    cout_even = -1
    for i in l1:
        cout_odd += 1
        odd_index.append(cout_odd)
    for i in odd_index:
        if i % 2 != 0:
            odd_elemnet.append(l1[i])
    print("Odd index number",odd_elemnet)
    for i in l2:
        cout_even += 1
        even_index.append(cout_even)
    for i in even_index:
        if i % 2 == 0:
            even_elemnet.append(l2[i])
    print("Even index number",even_elemnet)
    final_list = odd_elemnet + even_elemnet
    print("final_list",final_list)


l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
list(l1,l2)