stu = dict()

values = input().split()
name = values[0]
grades = list(map(int, values[1:]))
avg = sum(grades)/3
stu['name'] = name
stu['english'] = grades[0]
stu['python'] = grades[1]
stu['math'] = grades[2]
stu['avg'] = avg

grades.sort(reverse=True)

print('%s %.2f %.2f %.2f %.2f' % (stu['name'], grades[0], grades[1], grades[2], stu['avg']))

