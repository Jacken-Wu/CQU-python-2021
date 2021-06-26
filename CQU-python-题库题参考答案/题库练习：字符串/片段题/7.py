a = input()
i = 0
while i < len(a):
    if a[i].isdigit():

        a = a[:i] + a[i+1:]

        i = i - 1
    i = i + 1
print(a)

