# Convert list into dictionary and add new item into dictionary

def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    print(res_dct)
    res_dct.update({"name":"shiv"})
    print(res_dct)



lst = ['a', 1, 'b', 2, 'c', 3]
Convert(lst)