# coding=utf-8
"""
function examples
"""


# 可变参数
def f1(*args):
    [print(x) for x in list(args)]


# 任意参数
def f2(*args, **kw):
    print(args)
    print(kw)


# 默认参数
def f3(a, b, c=1, d=1):
    return list(zip([a, b], [c, d]))


# 生成器函数
def f4(start, end, step):
    while start <= end:
        yield start
        start += step


# 闭包
def f5(a):
    def add(b):
        return a + b

    return add


# 闭包实现计数器
def f6(begin=0):
    cnt = [begin]

    def add_one():
        cnt[0] += 1
        return cnt[0]

    return add_one


if __name__ == '__main__':
    f1("hello", 1, 2, 3)
    f2(1, 2, 3, a=1, b=2, c=3)
    print(f3(1, 2, c=3))

    [print(x) for x in f4(1, 5, 0.5)]

    print(f5(1)(2))

    counter1 = f6()
    print(counter1())   # 1
    print(counter1())   # 2

    counter2 = f6(5)
    print(counter2())   # 6
    print(counter2())   # 7
