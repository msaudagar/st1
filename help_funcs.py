def number_range(num1, num2, num_of_nums):
    num1 = round(num1, None)
    num2 = round(num2, None)
    diff = num2-num1
    step = diff/(num_of_nums-1)
    numslist = [num1]
    for idx in range(1,num_of_nums-1):
        numslist.append(round(num1+idx*step, None))
    numslist.append(num2)
    return numslist
