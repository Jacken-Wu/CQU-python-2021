def ji(n):
    if n % 2 == 0:
        return False
    return True


num = int(input())
if num == 0:
    print('green')
elif num in range(1, 11) or num in range(19, 29):
    if ji(num):
        print('red')
    else:
        print('black')
elif num in range(11, 19) or num in range(29, 37):
    if ji(num):
        print('black')
    else:
        print('red')
else:
    print('error')

