def find_list(l):
    l_2 = []
    for i in l:
        if type(i) == list:
            l_2 += i
    return l_2


l = eval(input())
find_needed = int(input())

for times in range(find_needed - 1):
    l = find_list(l)

print(len(l))

