GDP = dict()

key_value = input()
while key_value != 'ok':
    GDP[key_value.split(' ')[0]] = int(key_value.split(' ')[1])
    key_value = input()

GDP['China'] = 95
del GDP['Japan']

print(len(GDP))
print(GDP['USA'])

