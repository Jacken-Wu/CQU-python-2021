<<<<<<< HEAD
n = int(input())
l_1 = [1, 1]
l_2 = [0, 1]
s = 0
for i in range(n):
    l_1.append(l_1[-1] + l_1[-2])
    l_2.append(l_2[-1] + l_2[-2])
    s += l_1[-1] / l_2[-1]
print('%.4f' % s)
=======
n = int(input())
l_1 = [1, 1]
l_2 = [0, 1]
s = 0
for i in range(n):
    l_1.append(l_1[-1] + l_1[-2])
    l_2.append(l_2[-1] + l_2[-2])
    s += l_1[-1] / l_2[-1]
print('%.4f' % s)
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119

