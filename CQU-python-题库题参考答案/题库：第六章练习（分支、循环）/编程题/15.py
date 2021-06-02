sp = (3, 4, 5)
su = (6, 7, 8)
au = (9, 10, 11)
wi = (1, 2, 12)
m = int(input())
if m in sp:
    print('spring')
elif m in su:
    print('summer')
elif m in au:
    print('autumn')
elif m in wi:
    print('winter')
else:
    print('error')

