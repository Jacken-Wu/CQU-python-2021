class Student:
    def __init__(self, id, name, age, score):
        self.id = id
        self.name = name
        self.age = age
        self.score = score

    def show(self):
        print('sname:%s,sno:%s,sage:%s,score:%s' % (self.name, self.id, self.age, self.score))
    

l = input().split(',')
s = Student(l[0], l[1], l[2], l[3])
s.show()

