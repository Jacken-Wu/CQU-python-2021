n = eval(input())
even = 0 + n * 2
odd = 1 + n * 2
l1 = [x for x in list(range(n*2))[::2]
]
l2 = [x for x in list(range(n*2))[1::2]
]
l3 = []
for y in range(len(l1)):
    l3.append(l1[y]+l2[y])
print(l3)


