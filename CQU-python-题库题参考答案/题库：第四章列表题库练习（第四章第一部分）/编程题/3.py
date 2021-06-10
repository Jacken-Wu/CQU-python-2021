exec('lst = %s' % input())
sum = 0
for i in lst:
    sum += i
ave = sum / len(lst)
if ave % 1:
    print('%.2f' % ave)
else:
    print('%d' % ave)

