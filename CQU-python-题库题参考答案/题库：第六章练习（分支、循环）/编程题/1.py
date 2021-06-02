num = eval(input())
if num < 1000:
    print('%.2f' % 0)
elif num < 5000:
    print('%.2f' % (num * 0.02))
elif num < 10000:
    print('%.2f' % (num * 0.03))
else:
    print('%.2f' % (num * 0.05))

