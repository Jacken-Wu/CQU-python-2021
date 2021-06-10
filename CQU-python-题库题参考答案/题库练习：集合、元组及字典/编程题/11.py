<<<<<<< HEAD
你妈妈的 = {}
你奶奶的 = {}

傻逼 = input()
while 傻逼 != 'None':
    狗题库 = 傻逼.split()
    if 狗题库[0] not in 你妈妈的:
        你妈妈的[狗题库[0]] = 0
        你奶奶的[狗题库[0]] = 0
    你妈妈的[狗题库[0]] += float(狗题库[1])
    你奶奶的[狗题库[0]] += 1
    傻逼 = input()

垃圾东西 = list(zip(你妈妈的.keys(), 你奶奶的.values(), 你妈妈的.values()))
垃圾东西.sort(key=lambda 鬼: 鬼[0])
垃圾东西.sort(key=lambda 鬼: 鬼[1], reverse=True)
垃圾东西.sort(key=lambda 鬼: 鬼[2], reverse=True)

总价 = 0
总次数 = 0
狗次数 = 0
for 哈麻批 in 垃圾东西:
    print('%s %d %.2f' % 哈麻批)
    总价 += 哈麻批[2]
    总次数 += 哈麻批[1]
    if 哈麻批[1] > 狗次数:
        狗次数 = 哈麻批[1]

if 总价 != 0:
    print('%.2f' % (总价 / 总次数))

for 哈麻批 in 垃圾东西:
    if 哈麻批[1] == 狗次数:
        print(哈麻批[0], end=' ')
=======
你妈妈的 = {}
你奶奶的 = {}

傻逼 = input()
while 傻逼 != 'None':
    狗题库 = 傻逼.split()
    if 狗题库[0] not in 你妈妈的:
        你妈妈的[狗题库[0]] = 0
        你奶奶的[狗题库[0]] = 0
    你妈妈的[狗题库[0]] += float(狗题库[1])
    你奶奶的[狗题库[0]] += 1
    傻逼 = input()

垃圾东西 = list(zip(你妈妈的.keys(), 你奶奶的.values(), 你妈妈的.values()))
垃圾东西.sort(key=lambda 鬼: 鬼[0])
垃圾东西.sort(key=lambda 鬼: 鬼[1], reverse=True)
垃圾东西.sort(key=lambda 鬼: 鬼[2], reverse=True)

总价 = 0
总次数 = 0
狗次数 = 0
for 哈麻批 in 垃圾东西:
    print('%s %d %.2f' % 哈麻批)
    总价 += 哈麻批[2]
    总次数 += 哈麻批[1]
    if 哈麻批[1] > 狗次数:
        狗次数 = 哈麻批[1]

if 总价 != 0:
    print('%.2f' % (总价 / 总次数))

for 哈麻批 in 垃圾东西:
    if 哈麻批[1] == 狗次数:
        print(哈麻批[0], end=' ')
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119

