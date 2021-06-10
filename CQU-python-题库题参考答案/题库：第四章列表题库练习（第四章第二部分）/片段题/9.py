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
<<<<<<< HEAD






nums = eval(input())
y = search(nums)
print(y)
=======






nums = eval(input())
y = search(nums)
print(y)
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119


