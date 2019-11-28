import re

"""
正则表达式
    .match() 完全匹配
    .serach()   部分匹配
    .sub(pattern, want, source)
"""
p = re.compile(r'(\d+)-(\d+)-(\d+)')
print(p.match("2019-10-21").group(1))
print(p.match("2019-10-21").groups())

year, mon, day = p.match("2018-04-21").groups()
print("%s %s %s" % (year, mon, day))
