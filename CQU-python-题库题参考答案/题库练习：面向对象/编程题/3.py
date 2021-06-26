class Student:
    name = ''
    age = ''
    score = ''

    def __init__(self, name, age, score):
        Student.name = name
        Student.age = age
        Student.score = list(map(int, score))

    @classmethod
    def get_name(cls):
        return cls.name

    @classmethod
    def get_age(cls):
        return cls.age

    @classmethod
    def get_course(cls):
        return max(cls.score)


l = input().split(',')
s = Student(l[0], l[1], l[2:])
print('name:', s.get_name())
print('age:', s.get_age())
print('max_score:', s.get_course())

