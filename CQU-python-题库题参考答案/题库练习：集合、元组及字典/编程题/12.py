<<<<<<< HEAD
l = eval(input())
n = 0
for i in list(set(l)):
    if n < l.count(i):
        n = i

f = True
a = 0
b = 0
for i in range(len(l)):
    if l[i] == n and f:
        a = i
        f = False
    if l[i] == n:
        b = i

print(b - a + 1)
=======
l = eval(input())
n = 0
for i in list(set(l)):
    if n < l.count(i):
        n = i

f = True
a = 0
b = 0
for i in range(len(l)):
    if l[i] == n and f:
        a = i
        f = False
    if l[i] == n:
        b = i

print(b - a + 1)
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119

