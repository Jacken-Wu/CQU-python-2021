<<<<<<< HEAD
GDP = dict()

key_value = input()
while key_value != 'ok':
    GDP[key_value.split(' ')[0]] = int(key_value.split(' ')[1])
    key_value = input()

GDP['China'] = 95
del GDP['Japan']

print(len(GDP))
print(GDP['USA'])
=======
GDP = dict()

key_value = input()
while key_value != 'ok':
    GDP[key_value.split(' ')[0]] = int(key_value.split(' ')[1])
    key_value = input()

GDP['China'] = 95
del GDP['Japan']

print(len(GDP))
print(GDP['USA'])
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119

