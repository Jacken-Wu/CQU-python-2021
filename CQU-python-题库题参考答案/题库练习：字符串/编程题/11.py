def aba_aba(s):
    dic = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    l = []
    for c in s:
        if c in ['(', '[', '{']:
            l.append(c)
        elif c in [')', ']', '}']:
            if l == [] or c != dic[l[-1]]:
                return False
            else:
                del l[-1]

    return True


def run():
    # run你妈
    pass


if __name__ == '__main__':
    print(aba_aba(input()))

