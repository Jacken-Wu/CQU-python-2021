<<<<<<< HEAD
def backnum(n):
    n = str(n)
    for i in range(len(n) // 2):
        if n[i] != n[len(n) - i - 1]:
            return False
    return True


def sunum(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


num = int(input())
l = []
n_2 = 1
while len(l) != num:
    n_2 += 1
    if backnum(n_2) and sunum(n_2):
        l.append(n_2)

f = 0
for j in l:
    print('{:6}'.format(j),end='')
    f += 1
    if f == 10:
        print('')
        f = 0
=======
def backnum(n):
    n = str(n)
    for i in range(len(n) // 2):
        if n[i] != n[len(n) - i - 1]:
            return False
    return True


def sunum(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


num = int(input())
l = []
n_2 = 1
while len(l) != num:
    n_2 += 1
    if backnum(n_2) and sunum(n_2):
        l.append(n_2)

f = 0
for j in l:
    print('{:6}'.format(j),end='')
    f += 1
    if f == 10:
        print('')
        f = 0
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119

