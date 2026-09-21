"""
ndarray 数据操作练习
对应教材：chapter_preliminaries/ndarray.md
"""

import torch

## ndarray 初始化
a = torch.zeros((2,3,4))
print(a,end="\n\n")

b = torch.ones((2,3,4))
print(b)

# notes: 只支持0、1