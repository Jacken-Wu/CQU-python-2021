def print_matrix(n):
    l = [['0' for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            l[i][j] = str(min([i, j]) + 1)
    s = ''
    for i in l:
        s += ' '.join(i) + '\n'
    print(s)


number=eval(input())
print_matrix(number)



