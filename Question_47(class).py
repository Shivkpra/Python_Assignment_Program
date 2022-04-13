"""Count Occurance of each element from list
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
"""
class occurcenc_e:                                                  # creating class
    def __init__(self,sample_list):                                 # constructor
        self.sample_list=sample_list

    def occurcence(self,sample_list):                               #function declaration
        print(sample_list)
        cout_list = []
        for i in sample_list:
            cout = 0
            j = i + 1
            for j in sample_list:
                if i == j:
                    cout += 1                                       #increment the value of cout if element is repeated


            print(cout, end=" ")
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
obj=occurcenc_e(sample_list)                                        # creating object
obj.occurcence(sample_list)
