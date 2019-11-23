# coding=utf-8
"""
python data type:
    1) Number
    2) String
    3) List
    4) Tuple
    5) Set
    6) Dictionary

example of List blow
"""


def main():
    # 列表创建
    lis_num = [1, 2, 3]
    lis_str = ["iPhone", "iPad", "MacBook"]

    # 列表迭代
    for x in lis_num:
        print(x)
    for x in lis_str:
        print(x)

    # 列表访问
    print(lis_num[1])
    print(lis_num[1:2])
    print(lis_num[:2])
    print(lis_num[2:])

    print(lis_str[1])
    print(lis_str[1:2])
    print(lis_str[:2])
    print(lis_str[2:])

    # 列表更新
    lis_num[2] = "hello world"
    print(lis_num)

    # 列表删除
    del lis_num[2]
    print(lis_num)

    # 列表函数，方法
    print(len(lis_num))
    print(max(lis_num))
    print(min(lis_num))

    lis_num.append(12)
    print(lis_num)
    lis_num.sort(reverse=True)
    print(lis_num)

    # etc ...


if __name__ == '__main__':
    main()
