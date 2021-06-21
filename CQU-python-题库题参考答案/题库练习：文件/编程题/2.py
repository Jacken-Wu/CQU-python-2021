with open('in.txt') as f:
    s = f.read().split()

d = {}
for word in s:
    if word not in d:
        d[word] = 0
    d[word] += 1

l = list(d.items())
l.sort(key=lambda x: x[0])
l.sort(key=lambda x: x[1], reverse=True)

with open('out.txt', 'w') as f:
    for i in l:
        f.write('%s %d\n' % (i[0], i[1]))

