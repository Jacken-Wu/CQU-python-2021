def main():
    s = input()
    ch = input()
    print(count(s,  ch)
)


def count(s, ch):
    for i in range(len(s)):

        if ch == s[i]:
            return i

    return None


main()

