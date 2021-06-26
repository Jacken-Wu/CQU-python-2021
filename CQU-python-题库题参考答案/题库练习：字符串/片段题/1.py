def main():
    inword = input()
    print(plural(inword))

def plural(i):
    if i[-1] in ['s', 'x', 'o'] or i[-2:] in ['ch', 'sh']:
        return i + 'es'
    elif i[-1] == 'y':
        return i[:-1] + 'ies'
    return i + 's'


main()

