<<<<<<< HEAD
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
=======
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
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119

