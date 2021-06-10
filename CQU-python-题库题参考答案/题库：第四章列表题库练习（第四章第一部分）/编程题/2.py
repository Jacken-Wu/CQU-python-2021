exec('lst = %s' % input())
n, m = input().split(',')
n = int(n)
m = int(m)
if n >= len(lst) or m >= len(lst):
    print('error')
else:
    if n > m:
        i = n
        while i > m:
            lst.remove(lst[i])
            i -= 1
    else:
    	for i in range(n, m):
    	    lst.remove(lst[i])
    print(lst)

