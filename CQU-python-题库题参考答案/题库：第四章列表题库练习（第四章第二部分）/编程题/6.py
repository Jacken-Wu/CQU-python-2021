n = int(input())
list_0 = list(range(n + 1))
for i in range(n):
    list_0[i] = list_0[i + 1]
list_0.remove(list_0[0])
list_0[-1] = 1
print(list_0)


