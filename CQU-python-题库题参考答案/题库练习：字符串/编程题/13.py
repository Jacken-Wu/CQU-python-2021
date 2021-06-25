id = list(input())
l = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]

if len(id) == 18:
    s = 0
    for i in range(17):
        s += l[i] * int(id[i])

    n = s % 11
    m = (12 - n) % 11
    if id[-1] == 'X' and m == 10 or id[-1] == str(m):
        print('Correct')
    else:
        print('Wrong')
else:
    print('Error')

