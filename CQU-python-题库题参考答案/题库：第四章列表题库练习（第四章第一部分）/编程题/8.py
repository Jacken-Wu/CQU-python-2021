l = eval(input())
i = 0
try:
    while True:
        l.remove(0)
        i += 1
except:
    for j in range(i):
        l.append(0)
    print(l)


