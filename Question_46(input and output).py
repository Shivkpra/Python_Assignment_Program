"""Slice list into 3 chunks and reverse each chunks
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
"""
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print(sample_list)

length = len(sample_list)                                     #calculate length of list
chunk_size = int(length / 3)                                  # divide into 3 parts
print(chunk_size)
start=0
end=chunk_size
for i in range (3):                                           # loop will print 3 divided list  and its reversed
    indexes=slice(start,end)

    list_chunk = sample_list[indexes]
    print("Chunk ", i, list_chunk)
    print("Reversed",list(reversed(list_chunk)))
    start=end
    end+=chunk_size
