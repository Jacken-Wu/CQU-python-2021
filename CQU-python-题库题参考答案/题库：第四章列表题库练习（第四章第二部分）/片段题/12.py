def sumlist(n):
    s = 0
    for i in n:
        if type(i) == type([1, 2]):
            s += sumlist(i)
        else:
            s += i
    return s





nums = eval(input())
sumv = sumlist(nums)
print(sumv)


