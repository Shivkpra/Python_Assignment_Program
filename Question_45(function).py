"""Remove items from list
list1 = [54, 44, 27, 79, 91, 41]
Out
List After removing element at index 4  [34, 54, 67, 89, 43, 94]
List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]
"""
def modiify(sample_list):                                          #function declaration
    print("list ", sample_list)
    i = sample_list.pop(4)                                         # delete element from list of index 4
    print("After removing element at index 4      ", sample_list)

    sample_list.insert(2, 12)                                       # Add element in list at index 2
    print("List after Adding element at index 2   ", sample_list)

    sample_list.append(23)
    print("List after Adding element at last      ", sample_list)    # add element in list at last

sample_list = [34, 54, 67, 89, 11, 43, 94]
modiify(sample_list)                                                 #function call

