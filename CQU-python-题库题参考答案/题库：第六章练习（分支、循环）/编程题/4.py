<<<<<<< HEAD
num = int(input())
if num % (5 * 7 * 11) == 0:
    print('%d can divided by 5,7 and 11.' % num)
else:
    f = True
    if num % 5 == 0:
        print('%d can divided by 5.' % num)
        f = False
    if num % 7 == 0:
        print('%d can divided by 7.' % num)
        f = False
    if num % 11 == 0:
        print('%d can divided by 11.' % num)
        f = False
    if f:
        print('%d can not divided by 5,7 or 11.' % num)
=======
num = int(input())
if num % (5 * 7 * 11) == 0:
    print('%d can divided by 5,7 and 11.' % num)
else:
    f = True
    if num % 5 == 0:
        print('%d can divided by 5.' % num)
        f = False
    if num % 7 == 0:
        print('%d can divided by 7.' % num)
        f = False
    if num % 11 == 0:
        print('%d can divided by 11.' % num)
        f = False
    if f:
        print('%d can not divided by 5,7 or 11.' % num)
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119

