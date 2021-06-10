def change(n): #该函数需要返回5个值（可存入列表），即最优方案的总张数及各种钞票的张数，可以使用穷举法
    a = n // 25
    n -= 25 * a
    b = n // 10
    n %= 10
    c = n // 5
    n %= 5
    d = n
    s = a + b + c + d
    return s, a, b, c, d


number=eval(input())
result=change(number)
for x in result:
    print(x,end=" ")
    

