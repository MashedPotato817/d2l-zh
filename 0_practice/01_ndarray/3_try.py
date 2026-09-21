"""
ndarray 数据操作练习
对应教材：chapter_preliminaries/ndarray.md
"""

import torch

## 尝试 reshape 自动计算
a = torch.arange(18)
print(a)

b = a.reshape(3,-1)
print(b)

c = a.reshape(-1,3)
print(c)