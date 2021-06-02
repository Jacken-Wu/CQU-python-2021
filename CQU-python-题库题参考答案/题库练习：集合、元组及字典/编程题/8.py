stu = {"name": "Zhang", "english": 80, "python": 90, "math": 100}

s_1 = input().split()
s_2 = input().split()
s_3 = input().split()
stu1 = stu.copy()
stu2 = stu.copy()
stu3 = stu.copy()
l = ['name', 'english', 'python', 'math']
for i in range(1, 4):
    a = globals()['stu' + str(i)]
    b = globals()['s_' + str(i)]
    a[l[0]] = b[0]
    for j in range(1, 4):
        a[l[j]] = int(b[j])
    a['avg'] = round((a['english'] + a['python'] + a['math']) / 3, 2)
scores = [stu1, stu2, stu3]
scores.sort(key=lambda x: x['avg'], reverse=True)
print(scores)

