str_dict = dict()
str_tuple = input().split()

for s in str_tuple:
    if s not in str_dict:
        str_dict[s] = 0
    str_dict[s] += 1

l = list(str_dict.items())
l_2 = []
max_s = max(list(str_dict.values()))
for i in l:
    if i[1] == max_s:
        l_2.append(i)
l_2.sort()

for i in l_2:
    print(i[0], i[1])

