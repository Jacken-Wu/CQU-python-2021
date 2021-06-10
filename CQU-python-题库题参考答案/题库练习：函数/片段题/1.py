def sumlist(l, x):
    num = 0
    l_2 = []
    for i in l:
        if type(i) == list:
            l_2 += i
        else:
            num += i * x
    if l_2:
        num += sumlist(l_2, x+1)
    return num






nums = eval(input())
addv = sumlist(nums, 1)
print(addv)


