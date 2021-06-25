def ma(c):
    n = ord(c)
    if 65 <= n <= 90:
        return chr(155 - n)
    elif 97 <= n <= 122:
        return chr(219 - n)
    else:
        return c


def run():
    s = input()
    s_out = ''
    for c in s:
        s_out += ma(c)
    print(s_out)


if __name__ == '__main__':
    run()

