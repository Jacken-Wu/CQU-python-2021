def count(s):
    l = [0, 0, 0]
    for c in s:
        if c.isupper():
            l[0] += 1
        elif c.islower():
            l[1] += 1
        elif c.isdigit():
            l[2] += 1
    return l


def run():
    for i in count(input()):
        print(i)


if __name__ == '__main__':
    run()

