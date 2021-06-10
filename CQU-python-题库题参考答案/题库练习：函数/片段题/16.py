def digitSum(n):
    n_2 = str(n)
    n_3 = 0
    for i in n_2:
        n_3 += int(i)
    return n_3


a = int(input())
print(digitSum(a))

