names = input().split(',')
grades = eval(input())

list_0 = []
for i in range(len(names)):
    list_0.append([names[i], grades[i]])

print(list_0)


