# coding=utf-8


# with 语句
class Sample:
    def __enter__(self):
        print("enter")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("type: ", exc_type)
        print("val: ", exc_val)
        print("tb: ", exc_tb)

    @staticmethod
    def do_something():
        return "hello"


with Sample():
    Sample.do_something()


with open('./file', 'r') as file:
    for line in file.readlines():
        print(line.strip('\n'))
