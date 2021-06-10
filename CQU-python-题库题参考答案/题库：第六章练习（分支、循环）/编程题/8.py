h = float(input())
n = int(input())
s = -h
for i in range(n):
    s += h * 2
    h /= 2
print('%.2f' % s)

