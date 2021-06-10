def missNumber(n):
    i = 0
    while True:
        if i not in n:
            return i
        i += 1






nums = eval(input())
number = missNumber(nums)
print(number)


