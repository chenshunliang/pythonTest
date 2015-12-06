# from  math import sqrt
import cmath

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
