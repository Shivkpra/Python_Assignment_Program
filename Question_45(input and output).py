"""Remove items from list
list1 = [54, 44, 27, 79, 91, 41]
Out
List After removing element at index 4  [34, 54, 67, 89, 43, 94]
List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]
"""
sample_list = [34, 54, 67, 89, 11, 43, 94]

print("list ", sample_list)
i= sample_list.pop(4)                                        # delete element from list of index 4
print("After removing element at index 4      ", sample_list)

sample_list.insert(2, 45)                                    # Add element in list at index 2
print("List after Adding element at index 2   ", sample_list)

sample_list.append(87)                                       # add element in list at last
print("List after Adding element at last      ", sample_list)





