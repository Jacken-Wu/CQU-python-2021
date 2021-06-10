<<<<<<< HEAD
GDP = dict()

key_value = input()
while key_value != 'ok':
    GDP[key_value.split(' ')[0]] = int(key_value.split(' ')[1])
    key_value = input()

keys = list(GDP.keys())
values = list(GDP.values())
keys.sort()
values.sort()
india_in = 'no'
if 'India' in keys:
    india_in = 'yes'
sum_value = sum(values)

print(keys)
print(values)
print(india_in)
print(sum_value)
=======
GDP = dict()

key_value = input()
while key_value != 'ok':
    GDP[key_value.split(' ')[0]] = int(key_value.split(' ')[1])
    key_value = input()

keys = list(GDP.keys())
values = list(GDP.values())
keys.sort()
values.sort()
india_in = 'no'
if 'India' in keys:
    india_in = 'yes'
sum_value = sum(values)

print(keys)
print(values)
print(india_in)
print(sum_value)
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119

