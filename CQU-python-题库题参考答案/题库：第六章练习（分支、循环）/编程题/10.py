<<<<<<< HEAD
num = int(input())
f = True
if num > 999:
    num = 999
for n in range(100, num+1):
    a = n // 100
    b = n // 10 % 10
    c = n % 10
    if a**3 + b**3 + c**3 == n:
        print(n)
        f = False
if f:
    print('none')
=======
num = int(input())
f = True
if num > 999:
    num = 999
for n in range(100, num+1):
    a = n // 100
    b = n // 10 % 10
    c = n % 10
    if a**3 + b**3 + c**3 == n:
        print(n)
        f = False
if f:
    print('none')
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119

