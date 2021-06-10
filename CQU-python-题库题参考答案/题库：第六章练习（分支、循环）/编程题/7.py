<<<<<<< HEAD
l = []
while True:
    l.append(input())
    if l[-1] == '#':
        l.remove(l[-1])
        break
l_2 = map(int, l)
print(len(l), end=' ')
print(sum(l_2))
=======
l = []
while True:
    l.append(input())
    if l[-1] == '#':
        l.remove(l[-1])
        break
l_2 = map(int, l)
print(len(l), end=' ')
print(sum(l_2))
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119

