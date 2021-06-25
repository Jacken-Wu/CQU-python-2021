string = input()
s = ''

for c in string:
    num = ord(c)
    if 65 <= num <= 90:
        s += chr(155 - num)
    elif 97 <= num <= 122:
        s += chr(219 - num)
    else:
        s += c

print(string)
print(s)

