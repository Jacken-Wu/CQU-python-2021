string = input()
exec('list_1 = %s' % string)
sum = 0
for i in list_1:
  sum += i
print('%.2f' % (sum / len(list_1)))

