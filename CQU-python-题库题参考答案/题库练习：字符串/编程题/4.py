def find(s):
    l = list(map(str, list(range(10))))
    nums = []
    num = ''
    for c in s:
        if c in l:
            num += c
        elif num:
            nums.append(num)
            num = ''
    m = 0
    out = ''
    for i in nums:
        length = len(i)
        if length >= m:
            m = length
            out = i
    return out


def run():
    a = find(input() + 'a')
    if a:
        print(a)
    else:
        print('No digits')


if __name__ == '__main__':
    run()

