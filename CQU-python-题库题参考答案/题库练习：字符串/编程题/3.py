def count(s):
    dic = {}
    for i in s:
        if i not in dic:
            dic[i] = 0
        dic[i] += 1
    return dic


def run():
    s_1, s_2 = input(), input()
    if len(s_1) == len(s_2):
        print(count(s_1) == count(s_2))
    else:
        print(False)


if __name__ == '__main__':
    run()

