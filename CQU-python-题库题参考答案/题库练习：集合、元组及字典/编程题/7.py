<<<<<<< HEAD
moneys = {}
times = {}

string = input()
while string != 'None':
    string_1, string_2 = string.split()
    if string_1 not in moneys:
        moneys[string_1] = 0
        times[string_1] = 0
    moneys[string_1] += eval(string_2)
    times[string_1] += 1
    string = input()

l = list(zip(moneys.keys(), times.values(), moneys.values()))
l.sort(key=lambda x: x[0])
l.sort(key=lambda x: x[1], reverse=True)
l.sort(key=lambda x: x[2], reverse=True)

for n in l:
    print(n[0], n[1], '%.2f' % n[2])
=======
moneys = {}
times = {}

string = input()
while string != 'None':
    string_1, string_2 = string.split()
    if string_1 not in moneys:
        moneys[string_1] = 0
        times[string_1] = 0
    moneys[string_1] += eval(string_2)
    times[string_1] += 1
    string = input()

l = list(zip(moneys.keys(), times.values(), moneys.values()))
l.sort(key=lambda x: x[0])
l.sort(key=lambda x: x[1], reverse=True)
l.sort(key=lambda x: x[2], reverse=True)

for n in l:
    print(n[0], n[1], '%.2f' % n[2])
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119

