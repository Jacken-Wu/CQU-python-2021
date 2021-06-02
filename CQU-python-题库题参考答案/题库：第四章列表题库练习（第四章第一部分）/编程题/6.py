n, m, l = input().split(',')
n = int(n)
m = int(m)
l = int(l)

list_n = []
for i in range(m):
    list_n.append(n)
    n += l
print(list_n)

