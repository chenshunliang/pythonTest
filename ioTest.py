from io import StringIO
import os
import pickle

# f = open('/Volumes/CHEN\'S DISK/chen\'s python/pythonTest/pythonTest.txt', 'r')
# txt = f.read()
# print(txt)
# f.close()


# with StringIO('/Volumes/CHEN\'S DISK/chen\'s python/pythonTest/pythonTest.txt') as f:
#     print(f.readline())
#
# print(os.name)
# print(os.uname())
# print(os.path.abspath('.'))
# p = os.path.abspath('.')
# print(os.path.split(p))
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

# test
testPath = '/Volumes/CHEN\'S DISK/chen\'s python'


def getpathfiles(path):
    l = os.listdir(path)

    # print(l)

    def filterpath(name):
        return not os.path.isdir(os.path.join(path, name))

    def filterdir(name):
        return os.path.isdir(os.path.join(path, name))

    naff = list(filter(filterpath, l))
    # print(naff)
    newed = list(filter(filterdir, l))
    # print(newed)
    for nf in naff:
        print(os.path.join(path, nf))
    if len(newed) > 0:
        for d in newed:
            getpathfiles(os.path.join(path, d))


# getpathfiles(testPath)
# 序列化

d = dict(name='chen', age=18)
print(d)
f = open('/Volumes/CHEN\'S DISK/chen\'s python/pythonTest/pythonTest.txt', 'rb')
# pickle.dump(d, f)
x = pickle.load(f)
f.close()
print(x)
