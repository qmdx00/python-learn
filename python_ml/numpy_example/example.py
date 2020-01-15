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

# 矩阵乘法
a1 = np.array([[0, 2], [1, 0]])
a2 = np.array([[1, -2], [1, 0]])

m1 = np.mat([[0, 2], [1, 0]])
m2 = np.mat([[1, -2], [1, 0]])

# 矩阵相乘
print(np.dot(a1, a2))
print(np.matmul(a1, a2))
print(np.matmul(m1, m2))
print(np.dot(m1, m2))
print(m1 * m2)

# 对应位置乘积
print(a1 * a2)
print(np.multiply(a1, a2))
print(np.multiply(m1, m2))
