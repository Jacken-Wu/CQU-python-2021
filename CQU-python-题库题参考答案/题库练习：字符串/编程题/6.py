def zips(s):
    c_last = s[0]
    n = 0
    out = ''
    for c in s:
        if c == c_last:
            n += 1
        elif n == 1:
            out += c_last
            c_last = c
            n = 1
        else:
            out += c_last + str(n)
            c_last = c
            n = 1
    return out


def run():
    print(zips(input() + ' '))


if __name__ == '__main__':
    run()

