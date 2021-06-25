def digits(s):
    l = list(map(str, range(10)))
    for c in s:
        if c in l:
            return 1
    return 0


def low(s):
    for c in s:
        if ord(c) in range(97, 123):
            return 1
    return 0


def up(s):
    for c in s:
        if ord(c) in range(65, 91):
            return 1
    return 0


def length(s):
    if len(s) >= 8:
        return 1
    return 0


def ch(s):
    for c in s:
        if c in ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '-', '/', ',', '.', '?', '<', '>', ';', ':', '[', ']', '{', '}', '|', '\\']:
            return 1
    return 0


def run():
    s = input()
    print(sum([digits(s), low(s), up(s), length(s), ch(s)]))


if __name__ == '__main__':
    run()

