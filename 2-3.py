# coding: utf-8
"""
# 统计序列中元素出现的次数
# 1. zip
# 2. sorted
# 3. collections Counter most_common
"""
from random import randint
data = [randint(0,20) for _ in xrange(30)]
# res = {2:1, 3:2}
c  = dict.fromkeys(data, 0)
for x in data:
    c[x] += 1
# print c
print sorted(c.items(), key=lambda x: x[1])
# print {k:v for v,k in sorted([[v,k] for k, v in c.iteritems()])[-3:]}
# d = sorted(c)
# print list(iter(d))
print c.keys()
print c.values()
print zip(c.values(), c.keys())
print sorted(zip(c.itervalues(), c.iterkeys()))


from collections import Counter
c2 = Counter(data)
# print c2.most_common(3)

# 对于单词进行统计