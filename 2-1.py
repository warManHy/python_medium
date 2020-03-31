# coding: utf-8
"""
dict 过滤
"""

data = [2,3,4,5,1,1,5]

res = []
for x in data:
    if x >= 4:
        res.append(x)
    
print "first fuc", res


#filter 函数
from random import randint
import timeit

data = [randint(-10, 10) for _ in xrange(10)]
print data

fd = filter(lambda x: x >=0, data)

print fd

#list解析 更快
ld = [x for x in data if x >= 0]
print ld

# 字典
d = {x: randint(60,100) for x in xrange(1, 21)}
print d

nd = {k:v for k,v in d.iteritems() if v > 90}
print nd

#集合
s = set(data)
# print s
print {x for x in s if x % 3 == 0}