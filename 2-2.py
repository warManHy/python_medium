# coding: utf-8
# 元素命名

#enum 
NAME = 0
AGE = 1
SEX = 2
EMAIL = 3
# NAME,AGE,SEX,EMAIL = xrange(4)

student = ('jack', 13, 'male', '1233@qq.com')
print student[NAME], student[AGE]

# collections.namedtuple
from collections import namedtuple
Student = namedtuple('Student', ['NAME','AGE','SEX','EMAIL'])
s = Student('jim', 15, 'female', '233@11.com')
print s.NAME
