names = input().split(',')
grades = eval(input())
list_0 = []
for i in range(len(names)):
    list_0.append([names[i], grades[i]])
list_0.sort(key=lambda x: x[1])
print(list_0)


