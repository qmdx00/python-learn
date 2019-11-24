# coding=utf-8

file = open('./file', 'r')

for line in file.readlines():
    print(line.strip('\n'))

file.close()


