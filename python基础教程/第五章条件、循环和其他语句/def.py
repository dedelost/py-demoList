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
print zip(range(5),xrange(1000000))
a = range(10)
a = list(reversed(a))
print a
a = sorted(a)
print a
# break continue while
# for else 语句
for index in range(10):
    print index
    if index == 15:
        break
else:
    print 'output stream end!'
print [ x*x for x in range(10) if x % 3 ==0]
print [(x,y) for x in range(4) for y in range(4)]
girls = ['alice','bernice','clarice']
boys = ['charis','arnold','bob']
print [a + '+' + b for a in girls for b in boys if a[0] == b[0]]
# pass 空语句
# del 删除对象
# exec
exec 'print \'lol\''
