"""
Person class

tips:
    __sex__ 外界可见    可以被修改
    _sex    外部不可见  可以通过变量名修改
    __sex   外部不可见  无法通过变量名修改

"""


class Person:
    def __init__(self, name, age, sex):
        self._name = name
        self._age = age
        self._sex = sex

    def say_hello(self):
        print(
            "hello, my name is %s and i'm %d years old, i'm a %s" %
            (self._name, self._age, self._sex))
