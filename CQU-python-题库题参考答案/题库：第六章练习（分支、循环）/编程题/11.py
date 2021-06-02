num = int(input())
l = []
while num != 1:
    if num % 2 == 1:
        num *= 3
        num += 1
    else:
        num //= 2
    l.append(str(num))
print(','.join(l))

