tuple_input = input().split(' ')

sum_len = 0
for n in tuple_input:
    sum_len += len(n)

avg_len = sum_len / len(tuple_input)
print('%d,%.2f' % (len(tuple_input), avg_len))

