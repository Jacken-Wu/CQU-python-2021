<<<<<<< HEAD
strings = dict()

string = input()
while string != 'q':
    if string not in strings:
        strings[string] = 0
    strings[string] += 1
    string = input()

l = list(strings.items())
l.sort(key=lambda x: x[1])
print(l[-1][0], l[-1][1])
=======
strings = dict()

string = input()
while string != 'q':
    if string not in strings:
        strings[string] = 0
    strings[string] += 1
    string = input()

l = list(strings.items())
l.sort(key=lambda x: x[1])
print(l[-1][0], l[-1][1])
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119

