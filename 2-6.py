# coding: utf-8
"""
用户的历史记录功能
"""
from random import randint
from collections import deque

# d = deque([], 5)
# d.append(1)
# d.append(2)
# d.append(3)
# d.append(4)
# d.append(5)
# print d
# d.append(6)
# print d

N = randint(0, 100)
import pickle
# 将对象存在文件
# pick.dump(q, open("hi"), 'w')
# pick.load(open('hi'))
history = deque([], 5)

def guess(k):
    if k == N:
        print "right"
        return True
    if k < N:
        print "less"
    else:
        print "greater"
    return False

while True:
    line = raw_input("please input a number: ")
    if line.isdigit():
        k = int(line)
        history.append(k)
        pickle.dump(list(history), open('history','w'))
        if guess(k):
            break
    elif line == 'history' or line == "h?":
        # print list(history)
        with open('history') as f:
            data = pickle.load(f)
            print data
    elif line == 'quit':
        break

