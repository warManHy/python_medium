# coding: utf-8
"""
让字典保持有序
1. sorted
2. zip
3. colletions Counter
"""

d = {}
d['jim'] = (1, 35)
d['leo'] = (2, 37)
d['bob'] = (3, 40)

# 无序
# for k in d: print k

from collections import OrderedDict

d = OrderedDict()
d['jim'] = (2,35)
d['leo'] = (1, 20)
d['bob'] = (3,10)
# for k in d: print k

from time import time
from random import randint
from collections import OrderedDict
d = OrderedDict()
players = list('ABCDEFGH')
start = time()

for i in xrange(8):
    raw_input()
    p = players.pop(randint(0,7-i))
    end = time()
    print i + 1, p, end - start,
    d[p] = (i + 1, end -start)

print 
print '_' * 20
for k in d:
    print k, d[k]