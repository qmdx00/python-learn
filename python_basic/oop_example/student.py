"""
Student class
"""
from .person import Person


class Student(Person):
    def __init__(self, sid, name, age, sex):
        super().__init__(name, age, sex)
        self.__sid__ = sid

    def say_hello(self):
        print("student ID: %s, name: %s, age: %d, sex: %s" % (self.__sid__, self._name, self._age, self._sex))
