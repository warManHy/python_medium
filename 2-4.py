# coding: utf-8
"""
找出多个字典中的公共键
d1={"韩严":2,"特朗普":1}
d2={"韩x":2,"特朗普":1}
"""
from random import randint, sample

sample('abcdef', 3)

s1 ={x: randint(1,4) for x in sample('abcdef', randint(3, 6))}
# print s1
s2 ={x: randint(1,4) for x in sample('abcdef', randint(3, 6))}
s3 ={x: randint(1,4) for x in sample('abcdef', randint(3, 6))}

# print s1.viewkeys() 
# print s1.viewkeys() & s2.viewkeys() & s2.viewkeys()

print map(dict.viewkeys, [s1,s2,s3])

print reduce(lambda a,b: a & b, map(dict.viewkeys, [s1,s2,s3])) 

