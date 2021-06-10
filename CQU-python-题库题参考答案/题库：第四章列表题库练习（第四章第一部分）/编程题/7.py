<<<<<<< HEAD
list_s = eval(input())
for n_1 in range(97, 123):
    exec('%s = 0' % chr(n_1))
for string in list_s:
    for ii in string:
        for num in range(97, 123):
            if ii == chr(num):
                locals()[chr(num)] += 1

for n_1 in range(97, 123):
    n_2 = locals()[chr(n_1)]
    if n_2 != 0:
        print('%s,%d' % (chr(n_1), n_2))
=======
list_s = eval(input())
for n_1 in range(97, 123):
    exec('%s = 0' % chr(n_1))
for string in list_s:
    for ii in string:
        for num in range(97, 123):
            if ii == chr(num):
                locals()[chr(num)] += 1

for n_1 in range(97, 123):
    n_2 = locals()[chr(n_1)]
    if n_2 != 0:
        print('%s,%d' % (chr(n_1), n_2))
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119

