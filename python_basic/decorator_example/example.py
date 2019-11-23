"""
this is decorator example
"""
from functools import wraps


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
