# -*- coding:utf-8 -*-
from copy import deepcopy
# 初始化
dic={'a':1,'b':2}
print dic['a']

items = [('name','dede'),('age',34)]
items = dict(items)
print items

# 基本操作
# len
print len(items)
print items['name']
items['name'] = 'lost'
# del
del items['age']
# in
print  'name' in items
print 'name is %(name)s' % items
# clear()
items.clear()
print items
# copy()
items = dic.copy()
print items
items['a']=3
print items
print dic
# deepcopy()
items = deepcopy(dic)
print items
print dic
# fromkeys()
print {}.fromkeys(['x','y'])
# get()
print items.get('d')
# items()
print dic.items()
# iteritems()
print list(dic.iteritems())
# keys()
print dic.keys()
# iterkeys()
print list(dic.iterkeys())
# pop()
dic.pop('b')
# popitem()
dic.popitem()
# setdefault()
print dic.setdefault('height')
print dic
dic['c'] = 4
# update()
items = {'width':300}
dic.update(items)
print dic
# values()
print dic.values()
print list(dic.itervalues())