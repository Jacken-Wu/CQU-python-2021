import math

c1 = input()
c2 = input()
x1, y1 = c1.split(',')
x2, y2 = c2.split(',')
l = ['x1', 'x2', 'y1', 'y2']
for i in l:
    exec('%s = int(%s)' % (i, i))
s = pow((x1 - x2) ** 2 + (y1 - y2) ** 2, 0.5)
print('%.2f' % s)

