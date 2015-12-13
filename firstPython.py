# from  math import sqrt
from enum import Enum
import cmath
import logging
import unittest

# 正常曲直
print(1 / 2)
# 取整
print(1 // 2)

# 求余数
print(10 % 3)
# 求次方
print(2 ** 3)
print(pow(2, 3))

c = cmath.sqrt(-1)
print(c)

print('zhanglin')
print(repr('zhanglin'))

# 序列
l = '12345'
print(l[0])
print(l[-1])
print(l[-2])  # 倒数第二个数据  # 分片
# lSplit = l[1, 2]
print(l[1:5])
print(l[0:5:2])  # 按步长为2进行分片
print(l[0:5:-1])  # 按步长为2进行分片,倒排序

# 序列相加
print([1, 2, 3] + [4, 5, 6])
# 序列乘法
print([1, 2, 3] * 5)
print(repr(3) in l)
print('3' in l)

print(max([1, 2, 3, 3]))

listT = [1, 2, 3, 4]
del listT[2]
print(listT)


# 类
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    def __str__(self):
        return 'this is class %s' % self.__class__.__name__


stu = Student()
stu.score = 100

print(stu)


# 链式调用
class Chain(object):
    def __init__(self, path=''):
        self_path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


# url = Chain().users.repos
# print(Chain())
print(callable(Student))

# 枚举
Week = Enum('Week', ('Mon', 'Tus', 'Wen', 'Ths', 'Fir', 'Sat', 'Sun'))
for key, member in Week.__members__.items():
    print(key, '=>', member, ',', member.value)

print(Week.Mon)

# 异常
try:
    print(100 / 0)
except Exception as e:
    print('fail')
    # logging.exception(e)
finally:
    print('has exception')


# 单元测试
class TsetMy(unittest.TestCase):
    def test_add(self, a, b):
        self.assertTrue(isinstance(1, int))
