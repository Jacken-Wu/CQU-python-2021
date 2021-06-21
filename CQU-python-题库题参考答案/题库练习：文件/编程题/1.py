with open('data.txt') as f:
    s = f.read()

for c in s:
    n = ord(c)
    if 96 < n < 123:
        print(chr(n - 32), end='')
    else:
        print(c, end='')

