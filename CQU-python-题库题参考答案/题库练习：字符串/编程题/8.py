names = []
s = input()
while s != 'quit':
    names.append(s)
    s = input()

names.sort(key=lambda x: x.split()[0])
names.sort(key=lambda x: x.split()[1])

print(names)

