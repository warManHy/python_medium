# coding: utf-8
"""
生成器函数 yield实现可迭代对象
"""
def yield_fuc():
    print "fuc 1..."
    yield 1
    print "fuc 1..."
    yield 2

g = yield_fuc()
# print dir(g)
# print g.next()
# print g.next()
# print g.next()
# for x in g: print x

class PrimeNumber:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def isPrimeNum(self, k):
        if k < 2:
            return False
        for i in xrange(2, k):
            if k % i == 0:
                return False
        return True
    def __iter__(self):
        for k in xrange(self.start, self.end):
            if self.isPrimeNum(k):
                yield k

for x in PrimeNumber(1, 100): print x