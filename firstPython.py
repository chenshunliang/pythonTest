import sys


# print(sys.path)
# print(1 / 2)


# git test

class Student(object):
    __slots__ = ('name', 'score', 'age')

    def __int__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s : %s' % (self.name, self.score))


stu = Student()
stu.name = 'chen'
stu.score = 95
stu.print_score()

stu.age = 10
print(stu.age)
# stu.abc = 'abc'
# print(stu.abc)
