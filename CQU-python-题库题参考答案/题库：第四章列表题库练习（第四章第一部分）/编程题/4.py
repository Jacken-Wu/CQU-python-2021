string = input()
list_s = string.split(' ')
n, m = input().split(' ')
n = int(n)
m = int(m)
if n < len(list_s) and m < len(list_s):
    list_s[n], list_s[m] = list_s[m], list_s[n]
    print(list_s)
else:
    print('error')

