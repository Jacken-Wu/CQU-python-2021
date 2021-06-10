def print_matrix(n):
    l = [['0' for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            if i + j < n - 1:
                l[i][j] = '3'
            elif i + j == n - 1:
                l[i][j] = '1'
            else:
                l[i][j] = '2'
    s = ''
    for i in l:
        s += ' '.join(i) + '\n'
    print(s)


number=eval(input())
print_matrix(number)


