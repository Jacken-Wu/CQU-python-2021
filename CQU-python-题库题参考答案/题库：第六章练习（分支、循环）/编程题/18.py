<<<<<<< HEAD
num = list(map(int, list(input())))
length = len(num)

for i in range(length):
    num[i] = (num[i] + 5) % 10

for i in range(len(num) // 2):
    num[i], num[length - 1 - i] = num[length - 1 - i], num[i]

num = map(str, num)
print(''.join(num))
=======
num = list(map(int, list(input())))
length = len(num)

for i in range(length):
    num[i] = (num[i] + 5) % 10

for i in range(len(num) // 2):
    num[i], num[length - 1 - i] = num[length - 1 - i], num[i]

num = map(str, num)
print(''.join(num))
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119

