from pandas import Series, DataFrame

"""
pandas example
"""

# pandas Series 一维数据
arr = Series([1, 2, 3, 4])
print(arr)
print(arr.index)
print(arr.values)

arr1 = Series([2, 4, 6, 8], index=['a', 1, 2, 3])
print(arr1)
print('a' in arr1)
print(arr1.get('a'))

# pandas DataFrame 二维数据
data = {
    'city': ['shanghai', 'hangzhou', 'beijing', 'wuhan'],
    'year': [2018, 2019, 2016, 2017],
    'score': [1, 1.2, 1.5, 0.9]
}
# 初始化frame
frame = DataFrame(data, columns=['city', 'score', 'year'])
print(frame)
# 行列互换
print(frame.T)
# 获取对应的列数据
print(frame['score'])
print(list(frame['city']))

# 增加新的列
frame['cap'] = (frame.score >= 1)
print(frame.T)
