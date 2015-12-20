import os
import pickle
import time
import random
from multiprocessing import Pool, Process, Queue
import subprocess
import threading

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

print('process %s is start' % os.getpid())

#  多进程
# def long_time_task(name):
#     print('run task %s (%s)' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('task %s runs %0.2f seconds' % (name, (end - start)))
#
#
# if __name__ == '__main__':
#     print('parent process %s' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('waiting for all subprocess done...')
#     p.close()
#     p.join()
#     print('all subprocess done...')

# 子进程
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('exit code:', r)


# # 进程间通信
# def write(q):
#     print('process to write %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
#
# def read(q):
#     print('process to read %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('get %s from queue...' % value)
#
#
# if __name__ == '__main__':
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.terminate()


# 多线程
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>>%s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread is end %s' % threading.current_thread().name)


print('threading %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread is end %s' % threading.current_thread().name)
