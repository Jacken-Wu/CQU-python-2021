def f(i):
    s = 0
    for each in range(1, i+1):
        s += each / (each+1)
    return s

v=int(input())
print("%.4f" % f(v))

