"""ndarray 数据操作练习。

对应教材：chapter_preliminaries/ndarray.md
"""

import torch


def main():
    # 练习 1：创建包含 0 到 11 的张量，并观察它的值、形状和元素数量。
    x = torch.arange(12)
    print("x =", x)
    print("x.shape =", x.shape)
    print("x.numel() =", x.numel())

    # 练习 2：将 x 变形为 3 行 4 列，观察变形前后的元素。
    X = x.reshape(3, 4)
    print("X =", X)


if __name__ == "__main__":
    main()
