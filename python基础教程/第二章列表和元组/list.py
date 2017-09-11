# -*- coding:utf-8 -*-

#初始化
demos= ['hello','world','lol','xxx']
#index
print(demos[0])
#分片
print(demos[1:]);print(demos[0:]);print(demos[-1:])
#step
print(demos[0::2]);print(demos[1::2])
# 加法
temp = ['a','b','c','d']
print(demos+temp)
# 乘法
print(temp * 3)
#成员资格
print('a' in demos);print('lol' in temp);print('a' in temp);print('lol' in demos);
#len
print(len(demos))
#max
print(max(demos))
#min
print(min(demos))
#list函数
print(list('abcdefghijklmnopqrstuvwxyz'))
#元素赋值
demos[0]='hey';print(demos)
#删除元素
del demos[1]; print(demos)
#分片赋值
demos[1:2] = ['a','b'];print(demos)
#append
demos.append('haha');print(demos)
#count
print(demos.count('xxx'))
#extend
demos.extend(temp);print(demos)
#index
print(demos.index('a'))
#insert
demos.insert(4,'QQ');print(demos)
#pop
print(demos.pop())
#remove
demos.remove('QQ');print(demos)
#reverse
demos.reverse();print(demos)
#sort
demos.sort();print(demos)
demos.sort(key=len);print(demos)
demos.sort(cmp);print(demos)
demos.sort(reverse=True);print(demos)


#元组
demot=('a','b','c')
#tuple
print(tuple(demos))
print(demot[1])
