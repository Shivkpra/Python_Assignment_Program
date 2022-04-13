def  even_digit(end):
    lst=[]
    for i in range(0, end):
        flag = 1
        for j in str(i):
            if ord(j) % 2 != 0:
                flag = 0
        if flag == 1:
            lst.append(str(i))

    print(",".join(lst))
end=int(input("Enter the ending number:"))
even_digit(end)
