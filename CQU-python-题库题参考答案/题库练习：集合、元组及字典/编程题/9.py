with open('in.txt') as f:
    s = f.read().split()

dic = {}

for i in s:
    if i not in dic:
        dic[i] = 0
    dic[i] += 1

l = sorted(dic.items(), key=lambda x: x[0])
l.sort(key=lambda x: x[1], reverse=True)
for i in range(len(l)):
    l[i] = l[i][0] + ' ' + str(l[i][1]) + '\n'

with open('out.txt', 'w') as f:
    f.writelines(l)

