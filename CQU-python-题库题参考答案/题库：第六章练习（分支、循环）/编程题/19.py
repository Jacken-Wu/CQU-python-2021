n, m = map(int, input().split(' '))
l = []

if m - n < 3 or m > 10 or n < 0:
    print('illegal input')
else:
    for i in range(n, m):
        sum = 0
        if i != 0:
            sum += i
            sum *= 10
            for j in range(n, m):
                sum_2 = sum
                if j != i:
                    sum_2 += j
                    sum_2 *= 10
                    for k in range(n, m):
                        sum_3 = sum_2
                        if k != j and k != i:
                            sum_3 += k
                            l.append(sum_3)

print(' '.join(map(str, l)))

