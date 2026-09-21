"""
ndarray 数据操作练习
对应教材：chapter_preliminaries/ndarray.md
"""

import numpy as np

## 运算符
x = np.array([1, 2, 4, 8])
y = np.array([1, 1, 1, 1])

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x ** y)

z = np.exp(x)
print(z)