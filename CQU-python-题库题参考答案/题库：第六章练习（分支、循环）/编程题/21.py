<<<<<<< HEAD
def su(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


num = num_2 = int(input())
j = 2
l = []
while num != 1:
    if num % j == 0 and su(j):
        l.append(str(j))
        num /= j
    else:
        j += 1

print('%d=' % num_2 + '*'.join(l))
=======
def su(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


num = num_2 = int(input())
j = 2
l = []
while num != 1:
    if num % j == 0 and su(j):
        l.append(str(j))
        num /= j
    else:
        j += 1

print('%d=' % num_2 + '*'.join(l))
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119

