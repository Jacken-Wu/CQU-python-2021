class Student:
    count = 0
    sum = 0

    def __init__(self, id, name, age, score):
        self.id = id
        self.name = name
        self.age = age
        self.score = score
        Student.count += 1
        Student.sum += score

    @classmethod
    def avg(cls):
        print('stuCount:%d,scoreAve:%.1f' % (cls.count, cls.sum / cls.count))


l = input().split(',')
while l != ['End']:
    s = Student(l[0], l[1], l[2], int(l[3]))
    l = input().split(',')

try:
    s.avg()
except:
    print('stuCount:0,scoreAve:None')

