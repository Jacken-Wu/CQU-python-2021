l = []
while True:
    l.append(input())
    if l[-1] == '#':
        l.remove(l[-1])
        break
l_2 = map(int, l)
print(len(l), end=' ')
print(sum(l_2))

