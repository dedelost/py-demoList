# -*- coding:utf-8 -*-

# print and import
# as
import math as hey
print 'age',1
# 链式赋值
x = y = 'hey'
print x; print y;
# 增量赋值
a = 1;a += 1; print a
# 布尔
# false None 0 '' () [] {}  为假
#  and or not
try:
    assert a == 0
except AssertionError:
    print 'Error'

d = {'a':1,'b':2,'c':3}
for key,value in d.items():
    print key , value

names = ['lol','haha']
ages = [23,43,12]
print zip(names,ages)
for name , age in zip(names,ages):
    print name , '-', age