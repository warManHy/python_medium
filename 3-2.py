# coding: utf-8
"""
迭代对象和迭代器对象
"""
l = [1,2,3]
s = 'abcs'
# for x in l: print x
# for x in s: print x

# 可迭代 --> 迭代器
# print iter(l)
# print iter(s)
# print iter(5)

# print l.__iter__()
# print s.__getitem__

t = iter(l)
print t.next()
print t.next()
print t.next()
# StopIteration
# print t.next()

"""
1. 实现一个迭代器对象，next()
2. 实现一个可迭代对象，__iter__()返回一个迭代器对象
"""
import requests
# print getWeather(u'北京')
# print getWeather(u'西安')

from collections import Iterable, Iterator

class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0
    def getWeather(self, city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s %s %s' % (city, data['low'], data['high'])
    def next(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)

class WeathIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities
    def __iter__(self):
        return WeatherIterator(self.cities)

for x in WeathIterable([u'北京',u'西安',u'深圳']):
    print x
