import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8')


def num(s):
    l = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
    l_3 = ['', '拾', '佰', '仟', '万', '拾', '佰', '仟', '亿', '拾', '佰', '仟', '万']
    s = list(map(int, list(s)))[::-1]
    l_2 = []

    for i in s:
        l_2.insert(0, l_3[0])
        l_2.insert(0, l[i])
        l_3.remove(l_3[0])
    return l_2


def zero(l):
    l_2 = ['拾', '佰', '仟', '万', '亿']
    l_3 = []
    for i in range(len(l)-1, 0, -1):
        if l[i] in l_2 and l[i-1] == '零' and l[i] != '亿':
            del l[i]

    w = ''
    for c in l:
        if c != '零':
            l_3.append(c)
            w = ''
        elif w != '零':
            l_3.append(c)
            w = c

    if l_3[-2] == '零':
        del l_3[-2]

    for i in range(len(l_3)):
        if l_3[i] == '亿' and l_3[i-1] == '零':
            del l_3[i-1]
            break

    return l_3


def run():
    s = input()
    if s == '0':
        print('零元整')
    else:
        print(''.join(zero(num(s))) + '元整')


if __name__ == '__main__':
    run()

