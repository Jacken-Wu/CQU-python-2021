<<<<<<< HEAD
l = eval(input())
min = l[0]
max = l[0]
for i in l:
    if min > i:
        min = i
    if max < i:
        max = i

try:
    while True:
        l.remove(min)
except:
    pass

try:
    while True:
        l.remove(max)
except:
    pass

print(l)

# 笑死，这是什么乐色代码
=======
l = eval(input())
min = l[0]
max = l[0]
for i in l:
    if min > i:
        min = i
    if max < i:
        max = i

try:
    while True:
        l.remove(min)
except:
    pass

try:
    while True:
        l.remove(max)
except:
    pass

print(l)

# 笑死，这是什么乐色代码
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119
