def prime(n): #该函数有两个返回值，分别是素数个数和素数的和
    l = []
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            l.append(i)
    m = len(l)
    q = sum(l)
    return m, q


number=eval(input())
result=prime(number)
print(result[0],result[1])

