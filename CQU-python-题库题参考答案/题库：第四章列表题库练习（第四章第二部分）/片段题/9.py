def search(n):
    m = list(set(n))
    length = len(n)
    num = 0
    for i in m:
        while i in n:
            num += 1
            n.remove(i)
        if num > length / 2:
            return i
        else:
            num = 0
    return False






nums = eval(input())
y = search(nums)
print(y)


