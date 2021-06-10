l = eval('[' + input() + ']')
n, m = eval(input())
if -len(l) <= n < len(l):
    if n < 0:
        n = len(l) + n
    for i in range(m):
        l.append(l[n])
    print(l)
else:
    print('error')

