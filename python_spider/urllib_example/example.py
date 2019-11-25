from http.client import HTTPResponse
from urllib import request

"""
urllib example
"""

url = "http://www.baidu.com"

# 以下三种方式都可以让 pycharm 给出代码提示
res = request.urlopen(url, timeout=1)  # type: HTTPResponse
""":type : HTTPResponse"""
assert isinstance(res, HTTPResponse)

html = res.read().decode('utf-8').replace("\n", "").replace(" ", "")
print(html)
