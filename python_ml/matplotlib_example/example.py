from matplotlib import pyplot as plt
from pandas import Series

"""
Matplotlib example
"""

se = Series([1, 3, 2, 5, 7, 6], index=range(1, 7))
plt.plot(se)
plt.show()
