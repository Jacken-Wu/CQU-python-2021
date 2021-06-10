<<<<<<< HEAD
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
=======
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
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119

