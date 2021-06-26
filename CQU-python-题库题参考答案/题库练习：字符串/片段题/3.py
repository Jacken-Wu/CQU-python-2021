def main():
    a = input()
    print(strreduce(a))

def strreduce(a):
    b = ''
    for c in a:
        if c not in b:
            b += c
    return b


main()

