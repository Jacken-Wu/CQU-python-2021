def count_foreign(ids):
    s = 0
    for id in ids:
        if id[0] == 'L':
            s += 1
    return s


origin=input().split()
print(count_foreign(origin))

