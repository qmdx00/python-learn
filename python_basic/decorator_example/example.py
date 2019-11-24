# coding=utf-8
"""
this is decorator example
"""
from functools import wraps
import time


# 可变参数
def foo(*args, **kw):
    print("args = ", args)
    print("kw = ", kw)


foo(1, 2, 3, a=1, b=2)


# decorator 装饰器
def log(text):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            print('%s before %s' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log("execute")
def now():
    print("2019-11-22")


now()


# 装饰器模拟程序计时
def timer(tips="总共用了"):
    def inn(func):
        def wrapper():
            start_time = time.time()
            func()
            stop_time = time.time()
            print("%s %s" % (tips, stop_time - start_time))

        return wrapper

    return inn


@timer()
def test1():
    time.sleep(3)


@timer("程序运行了")
def test2():
    time.sleep(4)


test1()
test2()
