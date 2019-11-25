import numpy as np

"""
numPy example
"""

arr = np.array([1, 2, 3, 4.1])

print(arr.dtype)
print(arr)
print(arr + 2)

# 填充矩阵
print(np.zeros((3, 5)))
print(np.ones((3, 5)))

# 列表切片
a = np.arange(5)
print(a)
a[1:3] = 10
print(a)
