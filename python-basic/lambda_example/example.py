"""
this is python lambda and higher-order function example
"""
from functools import reduce, wraps

# lambda

f = lambda x, y: x + y
print(f(1, 2))

# map
lis1 = [1, 2, 3, 4]
print(list(map(lambda x: x * x, lis1)))
print(list(map(lambda x: str(x * x), lis1)))

# reduce
lis2 = [1, 3, 5, 7, 9]
print(reduce(lambda x, y: x + y, lis2))
print(reduce(lambda x, y: x * 10 + y, lis2))

# filter
lis3 = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda x: x % 2 == 0, lis3)))

# sorted
lis4 = [31, 5, 14, 27, -7]
print(sorted(lis4))
print(sorted(lis4, key=abs))
print(sorted(lis4, key=abs, reverse=True))
