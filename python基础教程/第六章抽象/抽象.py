# -*- coding:utf-8 -*-

def fib(num):
    'fibs function'
    fibs = [0,1]
    for x in range(num):
        fibs.append(fibs[-2]+fibs[-1])
    print fibs
print callable(fib)
fib(15)
print fib.__doc__
print help(fib)