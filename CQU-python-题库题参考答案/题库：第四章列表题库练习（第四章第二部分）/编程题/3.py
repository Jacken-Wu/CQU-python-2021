a = eval(input())  # 输入一个列表a
b = []  # 一个空列表
for i in a:
    if i == 1 or i == 0:  # 不是质数
        b.append(i)  # b
    for j in range(2, i):  # 2~i
        if i % j == 0:  # 整除
            b.append(i)  # 不是质数
            break
for i in b:
    a.remove(i)

print(a)

