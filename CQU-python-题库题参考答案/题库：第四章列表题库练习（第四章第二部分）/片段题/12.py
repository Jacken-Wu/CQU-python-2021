def sumlist(n):
    s = 0
    for i in n:
        if type(i) == type([1, 2]):
            s += sumlist(i)
        else:
            s += i
    return s
<<<<<<< HEAD





nums = eval(input())
sumv = sumlist(nums)
print(sumv)
=======





nums = eval(input())
sumv = sumlist(nums)
print(sumv)
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119


