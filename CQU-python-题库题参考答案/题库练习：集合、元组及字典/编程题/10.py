employee = {
    "0001": "Mary",
    "St0002": "Lee",
    "D0003": "Wang"
}
location = {}
sale = {}

sales = []
for i in range(int(input())):
    l = input().split()
    l[1] = int(l[1])
    sales.append(l)

for event in sales:
    l = event[0].split('-')
    location[l[0]] = l[1]
    if l[0] not in sale:
        sale[l[0]] = 0
    sale[l[0]] += event[1]

list_final = []
l = ['0001', 'St0002', 'D0003']
for i in l:
    try:
        list_final.append((location[i], employee[i], sale[i]))
    except:
        pass
list_final.sort(key=lambda x: x[2], reverse=True)
for i in list_final:
    print('%-10s%-10s%-10d' % i)

